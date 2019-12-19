# write a program squares of values in list print all values except first 5 values
def sqrslicing():
    l=[]
    for i in range(1,21):
        l.append(i**2)
    return l[5:]
print(sqrslicing())

def sqrslicing():
    l=[]
    for i in range(1,21):
        l.append(i**2)
    print(l[5:])
sqrslicing()
