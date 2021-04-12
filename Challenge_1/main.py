class prime:

    def __init__(self):
        min = int(input('Ingrese el valor minimo: '))
        max = int(input('Ingrese el valor maximo: '))
        print(self.num_generator(min, max))

    def num_generator(self, min, max):
        result = []
        for num in range(min, max):
            if self.PrimeNumberCheck(num):
                result.append(num)
        return result
    
    def PrimeNumberCheck(self, num):
        for x in range(2, num):
            if num % x == 0:
                return False
        return True

if __name__ == '__main__':
    prime()
        