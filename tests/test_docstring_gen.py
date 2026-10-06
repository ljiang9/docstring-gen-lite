import unittest

from docstring_gen import gen_docstring


class TestDocstring(unittest.TestCase):
    def test_basic(self):
        src = "def add(a, b):\n    return a + b\n"
        out = gen_docstring(src, "add")
        self.assertIn("Args:", out)
        self.assertIn("a", out)
        self.assertIn("b", out)

    def test_return_annotation(self):
        src = "def f(x: int) -> str:\n    return str(x)\n"
        out = gen_docstring(src, "f")
        self.assertIn("Returns:", out)
        self.assertIn("str", out)

    def test_skip_self(self):
        src = "class C:\n def m(self, x):\n  pass\n"
        out = gen_docstring(src, "m")
        self.assertIn("x", out)
        self.assertNotIn("self", out)

    def test_not_found(self):
        self.assertEqual(gen_docstring("def a():\n pass\n", "zzz"), "")


if __name__ == "__main__":
    unittest.main()
