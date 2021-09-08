class VowelCheck:

    def __init__(self, word):
        self.word = word
        self.vowelsVar = 'aeiou'

    def areThereVowels(self):
        for x in self.word:
            if x in self.vowelsVar:
                return True
        return False


