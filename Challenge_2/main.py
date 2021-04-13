class TextCounter:

    def __init__(self):
        text = open(r'Challenge_2\demo.txt').read()
        print('El texto ingresado es: ')
        print(text)
        print('1. El numero de caracteres en el texto es: ', self.CharCounter(text))
        print('2. El numero de palabras en el texto es: ', self.WordCounter(text))
        print('3. Las palabras repetidas son: ', self.RepeatWordCounter(text))
        print('4. El numero de parrafos son: ', self.ParragraphCounter(text))

    def CharCounter(self, text):
        counter = 0
        for char in text:
            if char != ' ':
                counter += 1
        return counter
    
    def WordExtractor(self, text):
        Words = text.split()
        return Words

    def WordCounter(self, text):
        WordsSize = len(self.WordExtractor(text))
        return WordsSize

    def RepeatWordCounter(self, text):
        Words = self.WordExtractor(text)
        RepeatWords = {}

        for Word0 in Words:
            if Word0 not in RepeatWords.keys():
                CounterBuffer = 0
                for Word1 in Words:
                    if Word0 == Word1:
                        CounterBuffer += 1
                if CounterBuffer > 1:
                    RepeatWords[Word0] = CounterBuffer

        return RepeatWords
    
    def ParragraphCounter(self, text):
        Parragraps = 1
        for i in range(0, len(text) - 1):
            if text[i] == '\n' and text[i + 1] == '\n':
                Parragraps += 1
        return Parragraps

if __name__ == '__main__':
    TextCounter()