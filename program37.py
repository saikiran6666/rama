# write a program squares of values in list print only first 5 values by using slicing
def sqrslice():
    l=[]
    for i in range(1,21):
        l.append(i**2)
    return l[:5]
print(sqrslice())