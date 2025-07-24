def num(x):
    if x==1 or x==2:
        return(1)
    return num(x-1)+num(x-2)
print(num(7))