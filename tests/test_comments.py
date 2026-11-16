from types import SimpleNamespace
import unittest
from unittest.mock import patch

import markdown

from generator import generator
from generator.extensions.comments import CommentExtension


class CommentExtensionTest(unittest.TestCase):
    def render(self, text):
        return markdown.markdown(
            text, extensions=["fenced_code", "pymdownx.superfences", CommentExtension()]
        )

    def test_inline_and_multiple_comments(self):
        self.assertEqual(
            self.render("Before %%hidden *markup*%%after %%second%%**bold**."),
            "<p>Before after <strong>bold</strong>.</p>",
        )

    def test_multiline_comment_with_blank_lines_and_html(self):
        self.assertEqual(
            self.render("Before\n\n%%\n<div>hidden</div>\n\n[link](secret)\n%%\n\nAfter"),
            "<p>Before</p>\n<p>After</p>",
        )

    def test_empty_and_comment_only_documents(self):
        for source in ("%%%%", "%%hidden%%", "%%\nhidden\n%%"):
            with self.subTest(source=source):
                self.assertEqual(self.render(source), "")

    def test_unclosed_comment_is_literal(self):
        self.assertEqual(self.render("Before %%unclosed"), "<p>Before %%unclosed</p>")

    def test_code_spans_are_literal(self):
        for source in (
            "`%%literal%%`",
            "``%%with `backtick`%%``",
            r"\\`%%literal%%`",
        ):
            with self.subTest(source=source):
                html = self.render(source + " %%hidden%%")
                self.assertIn("%%", html)
                self.assertNotIn("hidden", html)

    def test_fenced_code_is_literal(self):
        for source in (
            "```text\n%%literal%%\n```",
            "~~~text\n%%literal%%\n~~~",
            "````text\n%%literal%%\n`````",
            "> ```text\n> %%literal%%\n> ```",
        ):
            with self.subTest(source=source):
                html = self.render(source + "\n\n%%hidden%%")
                self.assertIn("%%literal%%", html)
                self.assertNotIn("hidden", html)

    def test_comments_in_list_continuations_are_removed(self):
        for source in (
            "- item\n    %%hidden%%",
            "- item\n\n    %%hidden%%",
            "1. item\n    %%hidden%%",
        ):
            with self.subTest(source=source):
                self.assertNotIn("hidden", self.render(source))

    def test_comment_boundaries_take_precedence_over_code_inside_comments(self):
        html = self.render("%%\n```text\nPRIVATE\n%%\n```\nAFTER")
        self.assertNotIn("PRIVATE", html)
        self.assertIn("AFTER", html)

    def test_commented_reference_definitions_are_not_registered(self):
        html = self.render("[label][hidden]\n\n%%\n[hidden]: https://secret.example\n%%")
        self.assertNotIn("<a", html)
        self.assertNotIn("secret.example", html)


class GeneratorCommentsTest(unittest.TestCase):
    def test_comments_removed_from_pages_and_rss_before_expansions(self):
        source = (
            "Visible %%[[Missing Page]] ![[hidden.png]] "
            "{ochrs:private}%% text"
        )
        with patch.dict(
            generator.ochrs_funcs,
            {"private": lambda: self.fail("Commented-out function was evaluated")},
        ):
            for rss in (False, True):
                with self.subTest(rss=rss):
                    self.assertEqual(
                        generator.process_markdown(source, rss=rss),
                        "<p>Visible  text</p>",
                    )

    def test_comments_in_unrendered_transcluded_bodies_are_removed(self):
        child = SimpleNamespace(title="Child", subtitle=None, body="Visible %%PRIVATE%%")
        with patch.object(generator, "tree", {"Child": child}), patch.object(
            generator, "tags", {"demo": {"Child"}}
        ):
            for rss in (False, True):
                html = generator.process_markdown(
                    "{ochrs:inline:demo:show-title}", rss=rss
                )
                self.assertIn("Visible", html)
                self.assertNotIn("PRIVATE", html)

    def test_fenced_code_in_transcluded_body_still_renders(self):
        child = SimpleNamespace(
            title="Child", subtitle=None, body="```text\ncode sample\n```"
        )
        with patch.object(generator, "tree", {"Child": child}), patch.object(
            generator, "tags", {"demo": {"Child"}}
        ):
            html = generator.process_markdown("{ochrs:inline:demo:show-title}")
            self.assertIn("<pre>", html)
            self.assertIn("code sample", html)

    def test_code_in_already_rendered_transcluded_bodies_is_preserved(self):
        for source in ("`%%literal%%`", "```text\n%%literal%%\n```"):
            child = SimpleNamespace(
                title="Child", subtitle=None, body=generator.process_markdown(source)
            )
            with patch.object(generator, "tree", {"Child": child}), patch.object(
                generator, "tags", {"demo": {"Child"}}
            ):
                for rss in (False, True):
                    with self.subTest(source=source, rss=rss):
                        html = generator.process_markdown(
                            "{ochrs:inline:demo:show-title}", rss=rss
                        )
                        self.assertIn("%%literal%%", html)

    def test_visible_generator_functions_still_expand(self):
        self.assertEqual(
            generator.process_markdown("{ochrs:example}"),
            "<p>{ochrs:func-name:arg1:arg2}</p>",
        )

    def test_generator_preserves_comment_examples_in_code(self):
        html = generator.process_markdown("```text\n%%{ochrs:page-count}%%\n```")
        self.assertIn("%%{ochrs:page-count}%%", html)


if __name__ == "__main__":
    unittest.main()
