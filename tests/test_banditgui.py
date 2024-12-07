import unittest
import sys
from unittest.mock import patch


class TestBanditGUI(unittest.TestCase):
    def test_module_docstring_exists(self):
        import banditgui

        self.assertIsNotNone(banditgui.__doc__)
        self.assertIn("BanditGUI", banditgui.__doc__)
        self.assertIn("main entry point", banditgui.__doc__)

    def test_module_docstring_format(self):
        import banditgui

        docstring = banditgui.__doc__
        self.assertTrue(docstring.strip().startswith('"'))
        self.assertTrue(docstring.strip().endswith('"'))

    @patch("sys.modules")
    def test_flask_import(self, mock_modules):
        import banditgui

        self.assertIn("flask", sys.modules)

    def test_docstring_sections(self):
        import banditgui

        docstring = banditgui.__doc__
        self.assertIn("This is the main entry point", docstring)
        self.assertIn("Flask application", docstring)
        self.assertIn("code organization", docstring)


if __name__ == "__main__":
    unittest.main()
