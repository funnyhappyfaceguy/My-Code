def fac(x):
    if x==1:
        return(1)
    return fac(x-1)*x
print(fac(5))