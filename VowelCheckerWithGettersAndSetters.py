class VowelCheck:

    def __init__(self, word):
        self.word = word
        self.vowelsVar = 'aeiou'

    def areThereVowels(self):
        for x in self.word:
            if x in self.vowelsVar:
                return True
        return False

    def getWord(self):
        return self.word

    def setWord(self, inp):
        self.word = inp

