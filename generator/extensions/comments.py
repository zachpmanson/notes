"""Obsidian-style %%comments%% for Python-Markdown."""

import re

from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor


# Recognize raw fences too: the generator strips comments once before ochrs
# expansion, then this extension strips comments in the expanded Markdown.
# Indentation alone cannot identify code (it may be a list continuation).
COMMENT_TOKENS = re.compile(
    r"^(?P<bi>[ \t]*(?:>[ \t]*)*)(?P<bf>`{3,})[^`\n]*\n"
    r".*?^(?P=bi)(?P=bf)`*[ \t]*(?:\n|$)"
    r"|^(?P<ti>[ \t]*(?:>[ \t]*)*)(?P<tf>~{3,})[^\n]*\n"
    r".*?^(?P=ti)(?P=tf)~*[ \t]*(?:\n|$)"
    r"|(?<!\\)(?:\\\\)*(?P<ticks>`+)(?!`)(?:(?!\n[ \t]*\n).)+?(?<!`)(?P=ticks)(?!`)"
    r"|(?P<comment>%%.*?%%)",
    re.MULTILINE | re.DOTALL,
)


class CommentPreprocessor(Preprocessor):
    def run(self, lines):
        text = COMMENT_TOKENS.sub(
            lambda match: "" if match.group("comment") is not None else match.group(),
            "\n".join(lines),
        )
        return text.split("\n")


class CommentExtension(Extension):
    def extendMarkdown(self, md):
        # Before fenced code (25), HTML blocks (20) and inline processing:
        # Markdown inside a comment must not hide its closing delimiter.
        md.preprocessors.register(CommentPreprocessor(md), "comments", 26)


def makeExtension(**kwargs):
    return CommentExtension(**kwargs)
