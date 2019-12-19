#write a program squares of values in list between 1,21 print last 5 values in list by using slicing
def sqrslicing():
    l=[]
    for i in range(1,21):
        l.append(i**2)
    return l[-5:]
print(sqrslicing())
