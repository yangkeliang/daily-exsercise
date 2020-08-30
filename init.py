# class Name():

#     def get_name(self,name):
#         self.name=name

#     def put_name(self):
#         print(self.name)

# a=Name()
# a.get_name(1)
# a.put_name()

class Name():
    def __init__(self,name):
        self.name=name
    def put_name(self):
        print(self.name)

a=Name(1)
a.put_name()



