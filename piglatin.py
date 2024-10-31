import re

class PigLatin:

    def __init__(self, phrase: str):
        self._phrase = phrase

    def get_phrase(self) -> str:
        if self._phrase == '':
            return 'nil'
        return self._phrase

    def translate(self) -> str:
        phrase = self.get_phrase()
        words = phrase.split(" ")

        translation = []

        for word in words:
            if word.count("-") > 0:
                hyphens = word.split("-")
                hyphen_word = ""
                for index, sub_word in enumerate(hyphens):
                    hyphen_word += self.process_word(sub_word)
                    if index < len(hyphens)-1:
                        hyphen_word += "-"
                word = hyphen_word
            else:
                word = self.process_word(word)

            translation.append(word)

        return ' '.join(translation)

    def process_word(self, word: str) -> str:
        new_word = word
        vowels = ("a", "e", "i", "o", "u")
        i = 0
        while new_word[0] not in vowels and i < len(new_word):
            new_word = new_word[1:] + new_word[0]
            i += 1

        if new_word.endswith("y"):
            new_word = new_word + "nay"
        elif new_word.endswith(vowels):
            new_word = new_word + "yay"
        else:
            new_word = new_word + "ay"

        return new_word

    def contains_invalid_chars(self, s: str) -> bool:
        pattern = r"[^a-zA-Z.,;:'?!()\s]"
        return bool(re.search(pattern, s))