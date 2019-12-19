# #write program given tuple of numbers find even numbers print
#
# tp=(1,2,3,4,5,6,7,8,98,100,99)
# l=[]
# for i in tp:
#     if(i%2==0):
#      l.append(i)
# print(tuple(l))

# t=(1,2,3,4,5,6,7,8,98,100,99)
# l=[]
# for i in tp:
#  if t[i]%2==0:
#      l.append(t[i])
# t1=tuple(l)
# print(t1)
def eventup():
    t = (1, 2, 3, 4, 5, 6, 7, 8, 98, 100, 99)
    l = []
    for i in t:
        if (i % 2 == 0):
            l.append(i)
    return l
print(eventup())
