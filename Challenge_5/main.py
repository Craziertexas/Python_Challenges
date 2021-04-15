class Calculation:

    def __init__(self):
        self.PrintMenu()
        input = self.GetInput()
        self.Selector(input)
    
    def PrintMenu(self):
        print('Select the Calculation: ')
        print('1. Factorial')
        print('2. Exponential')
        print('3. Exponential of X')

    def GetInput(self):
        sw_input = True
        while sw_input:
            try:
                selection = int(input('Select: '))
                sw_input = False
            except:
                sw_input = True
        return selection
    
    def Selector(self, input):
        success = False
        if input == 1:
            print('Factorial of: ')
            num = self.GetInput()
            print('Result: ')
            print(self.Factorial(num))
            success = True

        elif input == 2:
            print('Value of exponent: ')
            print('Result: ')
            print(self.Exponent(1))
            success = True

        elif input == 3:
            print('Exponent of: ')
            num = self.GetInput()
            print('Result: ')
            print(self.Exponent(num))
            success = True

        else:
            print('Input not specified')
        
        return success
    
    def Factorial(self, num):
        result = 1
        for x in range(1,num+1):
            result = result*x
        return result
    
    def Exponent(self,num):
        result = 1
        for x in range(1,1000):
            result = ((num**x)/self.Factorial(x)) + result
        return result

if __name__ == '__main__':
    Calculation()