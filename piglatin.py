class PigLatin:

    def __init__(self, phrase: str):
        self._phrase = phrase

    def get_phrase(self) -> str:
        if self._phrase == '':
            return 'nil'
        return self._phrase

    def translate(self) -> str:
        phrase = self.get_phrase()
        vowels = ("a","e","i","o","u")
        i = 0
        while phrase[0] not in vowels and i < len(phrase):
            phrase = phrase[1:] + phrase[0]
            i += 1

        if phrase.endswith("y"):
            return phrase + "nay"
        elif phrase.endswith(vowels):
            return phrase + "yay"
        return phrase + "ay"