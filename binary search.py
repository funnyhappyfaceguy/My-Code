binary=[2,4,6,8,9,12,15]
def search(start,end,target):
    x=0
    x=round((start+end)/2)
    if binary[x]==target:
        return(x)
    if target<=binary[x]:
        end=x-1
        return search(start,end,target)
    if target>=binary[x]:
        start=x+1
        return search(start,end,target)
print(search(0,6,15))