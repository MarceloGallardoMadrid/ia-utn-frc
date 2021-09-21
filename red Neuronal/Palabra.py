class Palabra:
    def __init__(self,word):
        self.word=word
    def __add__(self,other):
        return Palabra(self.word+"+"+other.word)
    def __mul__(self,other):
        return Palabra(self.word+"*"+other.word)
    def toString(self):
        return self.word
    def __str__(self):
        return self.word