
a=10
print ("hi",a)
#b=input("enter value : ")
#print(b)


def func(b):
    #b=120
    print("This is independent function")
    print(b)
    c=int(b)+100
    print(c)

func('311')

class A:
    #def __init__(self,g):
     #   print("Constructor value ",g)

    def func1(self):
        print("function in class A")
        d=30
        print(d)

    def func2(self,e):
        print("func2 in class A")
        print(e)
#obj=A(80)
obj=A()
obj.func1()
obj.func2(40)