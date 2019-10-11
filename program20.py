# by using generator number divisible by 7 with in the range

def putNumbers(n):
    i=0
    while i<n:
        for j in range(n):
            if j%7==0:
                yield j
            i+=1
n=putNumbers(40)
print(list(n))


