class crypter:

    def __init__(self):
        num = int(input('Ingrese el valor a encriptar: '))
        print(self.cryp(num))

    def cryp(self, num):
        digits = self.DigitsSeparator(num)
        digits = self.DigitsSum(digits, 7)
        digits = self.DigitsModule(digits, 10)
        digits = self.DigitsInterchange(digits, [3 , 4, 1, 2])
        return digits

    def DigitsSeparator(self, num):
        digits = []
        for d in str(num):
            digits.append(int(d))
        return digits
    
    def DigitsSum(self, digits, increment):
        newdigits = []
        for d in digits:
            newdigits.append(d + increment)
        return newdigits
    
    def DigitsModule(self, digits, divider):
        newdigits = []
        for d in digits:
            newdigits.append( d % divider)
        return newdigits

    def DigitsInterchange(self, digits, order):
        newdigits = []
        for i in order:
            newdigits.append(digits[i - 1])
        return newdigits
        
if __name__ == '__main__':
    crypter()