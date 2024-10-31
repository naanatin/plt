class PigLatin:

    def __init__(self, phrase: str):
        self._phrase = phrase

    def get_phrase(self) -> str:
        if self._phrase == '':
            return 'nil'
        return self._phrase

    def translate(self) -> str:
        phrase = self.get_phrase()
        if not phrase.startswith(("a","e","i","o","u")):
            phrase = phrase[1:] + phrase[0]
        if phrase.endswith("y"):
            return phrase + "nay"
        elif phrase.endswith(("a","e","i","o","u")):
            return phrase + "yay"
        return phrase + "ay"