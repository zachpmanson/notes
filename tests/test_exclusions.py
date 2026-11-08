import copy
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from generator import generator


class ExcludedDirectoriesTest(unittest.TestCase):
    def test_templates_are_excluded_at_every_depth(self):
        tree = {"Index": copy.deepcopy(generator.tree["Index"])}
        routes = {"Index": "./"}
        original_cwd = Path.cwd()
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for name in (
                "Published.md",
                "Group/Visible.md",
                "Templates/Line Template.md",
                "Templates/Nested/Hidden.md",
                "Group/Templates/Nested Template.md",
            ):
                path = root / "notes" / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("Example note", encoding="utf-8")
            try:
                os.chdir(root)
                with patch.object(generator, "tree", tree), patch.object(
                    generator, "routes", routes
                ):
                    generator.get_tree()
            finally:
                os.chdir(original_cwd)
        self.assertEqual(set(tree), {"Index", "Published", "Group", "Visible"})
        self.assertEqual(set(routes), set(tree))
        self.assertEqual(tree["Index"].children, {"Published", "Group"})
        self.assertEqual(tree["Group"].children, {"Visible"})


if __name__ == "__main__":
    unittest.main()
