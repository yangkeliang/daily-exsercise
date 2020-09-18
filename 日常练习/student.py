class Student():
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score
        
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def get_course(self):
        return max(self.score)

ykl=Student('ykl',26,[100,99,98])

print(ykl.get_name())
print(ykl.get_age())
print(ykl.get_course())