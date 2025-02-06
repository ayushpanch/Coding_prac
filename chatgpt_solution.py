class Calculator:
    def addition(self, num1, num2):
        return num1 + num2

    def subtraction(self, num1, num2):
        return num1 - num2

if __name__ == "__main__":
    calc = Calculator()

    # Test addition
    result_add = calc.addition(5, 3)
    print("Addition Result:", result_add)

    # Test subtraction
    result_sub = calc.subtraction(8, 3)
    print("Subtraction Result:", result_sub)