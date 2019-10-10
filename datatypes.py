#data types
#1.int,float,complex,bool,str,bytes,bytearrary,range,list,tuple,set,dictionary,frozenset,None
#int
#ways:1 decimal form
     # 2 binary form
     # 3 octal form
     # 4hexa octal form
# decimal
# 0 to 9
# binary the number start with 0b.0B only taken as binary
# a=ob1111
# a=oB1111
#binary number example
a=0B1111
print(a)
a=-0b1111
print(a)
#octal number example start with 0o only taken as octal
a=0o1111
print(a)
#hexa decimal example start with 0x and name in between a to f only
a=0xface
print(a)
list1=[1,2,3,4,5]
list2=[6,7,8,9,10]
list=[]
for i in range(0,len(list1)):
  list.append(list1[i]+list2[2])
print("result list is:" +str(list))






