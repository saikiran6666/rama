#write a program given tuple values print first half values in one tuple and last half values in one tuple
tuple=(1,2,3,4,5,6,7,8,9,10)
tuple1=tuple[:5]
tuple2=tuple[5:]
print(tuple1)
print(tuple2)

def halfval():
    fl=[]
    sl=[]
    tup=(1,2,3,4,5,6,7,8,9,10)
    l=len(tup)/2
    for i in range(1,int(l)+1):
        fl.append(i)
    for j in range(int(l+1),int(len(tup)+1)):
        sl.append(j)
    print(fl)
    print(sl)
halfval()
