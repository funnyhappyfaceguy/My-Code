def add(x,y):
    z=x+y
    print(str(x)+" + "+str(y)+" = "+str(z))
    print("The Sum is "+str(z))
def sub(x,y):
    z=x-y
    print(str(x)+" - "+str(y)+" = "+str(z))
    print("The Sum is "+str(z))
def div(x,y):
    z=x/y
    print(str(x)+" / "+str(y)+" = "+str(z))
    print("The Quotient is "+str(z))
def mult(x,y):
    z=x*y
    print(str(x)+" * "+str(y)+" = "+str(z))
    print("The Product is "+str(z))

b=10
while b>0:
    a=int(input("1 for Addtion, 2 for Subtraction, 3 for Multiplication and 4 for Division: "))
    while a==1:
        x=int(input("What is the First Number? "))
        y=int(input("What is the Second Number? "))
        add(x,y)
    while a==2:
        x=int(input("What is the First Number? "))
        y=int(input("What is the Second Number? "))
        sub(x,y)
    while a==3:
        x=int(input("What is the First Number? "))
        y=int(input("What is the Second Number? "))
        mult(x,y)
    while a==4:
        x=int(input("What is the First Number? "))
        y=int(input("What is the Second Number? "))
        div(x,y)