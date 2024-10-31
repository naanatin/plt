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
        vowels = ("a","e","i","o","u")
        translation = []

        for word in words:
            i = 0
            while word[0] not in vowels and i < len(word):
                word = word[1:] + word[0]
                i += 1

            if word.endswith("y"):
                word = word + "nay"
            elif word.endswith(vowels):
                word = word + "yay"
            else:
                word = word + "ay"

            translation.append(word)

        return ' '.join(translation)