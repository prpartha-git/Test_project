#from selenium.webdriver import chrome
#driver=chrome()

#driver.findelement.by.xpath()

print("This is sample Python prog")
a=input("Enter a number")
print(a)
c=20+int(a)
print("Sum is ",c)
d=int(a)
if(int(a)>100):
    print("A is Greater than 100",a)
else:
    print("A is Smaller", a)

if(d>0):
    print("D is greater than 0")
elif(d==0):
    print("D = Zero")
else:
    print("D is less than 0")

#Nested if else condition
e=d
if(e>0):
    if(e%2==0):
        print("Number is Even")
    else:
        print("Number is Odd")
else:
    print("Number is Negative")