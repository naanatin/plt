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
        self._word = word
        vowels = ("a", "e", "i", "o", "u")
        i = 0
        while self._word[0] not in vowels and i < len(self._word):
            self._word = self._word[1:] + self._word[0]
            i += 1

        if self._word.endswith("y"):
            self._word = self._word + "nay"
        elif self._word.endswith(vowels):
            self._word = self._word + "yay"
        else:
            self._word = self._word + "ay"

        return self._word