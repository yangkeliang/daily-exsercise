class Dic():
    def __init__(self,diky):
        self.diky=diky
    
    def del_key(self,i):
        del self.diky[i]

    def get_key(self,i):
        if i in self.diky:
            print (self.diky[i])
        else:
            print("not found")

    def get_keylist(self):
        list=[]
        for i in self.diky:
            list.append(i)
        return list

    def update_dic(self,diky):
        diky.update(self.diky)
        list=[]
        for i in diky:
            list.append(i)
        return list



dic=Dic({1:"dsa",2:"gfh",3:"jje"})

print(dic.update_dic({4:3,9:0,8:9}))

# print(dic.diky)

# dic.del_key(1)

# print(dic.diky)

# print(dic.diky)

# dic.get_key(6)

# print(dic.get_keylist())


        
