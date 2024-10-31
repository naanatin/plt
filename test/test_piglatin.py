import unittest
from piglatin import PigLatin
from error import PigLatinError


class TestPigLatin(unittest.TestCase):

    def test_get_phrase(self):
        translator = PigLatin("hello world")

        self.assertEqual("hello world", translator.get_phrase())

    def test_empty_phrase(self):
        translator = PigLatin("")

        self.assertEqual("nil", translator.get_phrase())

    def test_translator_ends_with_y(self):
        translator = PigLatin("any")

        self.assertEqual("anynay", translator.translate())