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

    def test_translator_ends_with_vowel(self):
        translator = PigLatin("apple")
        self.assertEqual("appleyay", translator.translate())

    def test_translator_ends_with_consonant(self):
        translator = PigLatin("ask")
        self.assertEqual("askay", translator.translate())

    def test_translator_move_consonant(self):
        translator = PigLatin("hello")
        self.assertEqual("ellohay", translator.translate())

    def test_translator_move_two_consonants(self):
        translator = PigLatin("known")
        self.assertEqual("ownknay", translator.translate())

    def test_translator_one_consonant(self):
        translator = PigLatin("k")
        self.assertEqual("kay", translator.translate())

    def test_translator_move_three_consonants(self):
        translator = PigLatin("tski")
        self.assertEqual("itskay", translator.translate())