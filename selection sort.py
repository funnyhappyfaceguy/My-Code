select=[4,5,8,2,6,3,1,7,9]
a=0

def small(a):   
    x=a
    for j in range(a,len(select)):
        if select[x]>select[j]:
            x=j
    return(x)

for i in range(len(select)-1):
    b=small(a)
    y=select[b]
    z=select[i]
    select[b]=z
    select[i]=y
    a=a+1
    print(select)

# for i in range(round(len(select)/2)):
# small(a)
    
#     for j in range(len(select)-1):
#         if select[0+j]>select[1+j]:
#             x=select[0]
#             y=select[len(select)-1]
#             select[0]=y
#             select[len(select)-1]=x

#     a=a+1
   
# print(small(a))