#write a program squares of numbers in list between 1,21 and conver the output into tuple
def printtuple():
    l=[]
    for i in range(1,21):
        l.append(i**2)
    print(tuple(l))
printtuple()