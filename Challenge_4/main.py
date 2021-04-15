class decryption:

    def __init__(self):
        num = input('Ingrese el valor a desencriptar: ')
        print(self.decrypt(num))

    def decrypt(self, num):
        digits = self.DigitsSeparator(num)
        digits = self.DigitsInterchange(digits, [3, 4, 1, 2])
        digits = self.DigitModInverse(digits)
        return digits

    def DigitsSeparator(self, num):
        digits = []
        for d in num:
            digits.append(int(d))
        return digits

    def DigitsInterchange(self, digits, order):
        newdigits = []
        for i in order:
            newdigits.append(digits[i - 1])
        return newdigits

    def ModInverse(self, num, mod):
        ModValues = []
        solution = -1
        for x in range(0, 10):
            ModValues.append( (x+7) % mod)

        for x in range(0, 10):
            if num == ModValues[x]:
                solution = x
        
        return solution
    
    def DigitModInverse(self, digits):
        newdigits = []
        for d in digits:
            newdigits.append(self.ModInverse(d, 10))
        return newdigits

if __name__ == '__main__':
    decryption()