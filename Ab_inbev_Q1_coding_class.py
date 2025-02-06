class calculator:

    def __init__(self,variable1,variable2):
        self.variable1 = variable1
        self.variable2 = variable2
        print(f"this is a constructor ---- {self.variable1 + self.variable2}")


    def addition(self,variable1,variable2):
        return variable1 + variable2
    
    def substraction(self,variable1,variable2):
        return variable1 - variable2


if __name__ == "__main__":
    object_of_calculator_class = calculator(12,12)
    addition_1 = object_of_calculator_class.addition(12,12)
    substraction_1 = object_of_calculator_class.substraction(24,12)
    print(f"the addition is ---------- {addition_1}")
    print(f"the substraction is ------------- {substraction_1}")


    
