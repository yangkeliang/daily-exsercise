def oouter(i):
    def outer(fun):
        def inner(*para):
            print("杨可亮的第{}个函数：".format(i))
            fun(*para)
        return inner
    return outer

@oouter(1)
def add(a,b):
    print("{}+{}={}".format(a,b,a+b))

@oouter(2)
def sub(a,b):
    print("{}-{}={}".format(a,b,a-b))

@oouter(3)
def div(a,b):
    print("{}/{}={}".format(a,b,a/b))

add(1,2)
sub(1,2)
div(1,2)