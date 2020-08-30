class calculator():
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        print(self.num1+self.num2)
    def sub(self):
        print(self.num1-self.num2)
    def mul(self):
        print(self.num1*self.num2)
    def div(self):
        print(self.num1/self.num2)

calculator(1,2).div()
    
# class calculator():
#     def __init__(self):
#         pass
#     def add(self,num1,num2):
#         print(num1+num2)

# calculator().add(1,2)