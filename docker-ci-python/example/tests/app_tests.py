import unittest

from example.app import get_some_magic


class MagicTest(unittest.TestCase):

    def test_the_magic(self):
        self.assertEqual("Magic!!", get_some_magic())
