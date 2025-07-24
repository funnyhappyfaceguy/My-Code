bubble=[15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,-1,-2,-3,-4,-5]
for i in range(len(bubble)-1):
    for j in range(len(bubble)-1):
        if bubble[0+j]>bubble[1+j]:
            x=bubble[0+j]
            y=bubble[1+j]
            bubble[0+j]=y
            bubble[1+j]=x
    print(bubble)