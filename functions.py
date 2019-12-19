# example of function
# def my_function():
#   print("Hello from a function")
#
# #calling functions
# def my_function():
#     print("hello mani kishore")
# my_function()
#
# #give parameters to function
# def my_function(fname):
#     print(fname +" mani")
# my_function("mani")
# my_function("kishore")
# my_function("kiran")
#
# #default parameter value
# def my_function(country=  "india"):
#     print("i am from " + country)
# my_function("america")
# my_function("koria")
# my_function("narwey")
# my_function()
#
# #passing a list as a parameter
# def my_function(fruits):
#     for x in fruits:
#         print(x)
# fruits=["apple", "banana", "cherry"]
# my_function(fruits)
#
# # return() ststement used in functions
# def my_function(x):
#     return 5 * x
# print(my_function(3))
# print(my_function(5))
# print(my_function(6))
# #
# # #keyword arguments
# def my_function(child1,child2,child3):
#     print("the youngest child " + child3)
# my_function(child1="mani",child2="kiran",child3="balaji")
# #
# #arbitary arguments
# def my_function(*kids):
#     print("the youngest child is "+kids[2])
# my_function("mani","kiran","balaji")
# # tri_recursion(6)
def tri_recursion(k):
    if(k>0):
      result=k+tri_recursion(k-1)
      print(result)
    else:
      result = 0
    return result
print("\n\nrecursion example results")
tri_recursion(2)


def cal(a,b):
    sum=a+b
    sub=a-b
    mul=a*b
    div=a/b
    return sum,sub,mul,div
t=cal(100,200)
for x in t:
    print(x)

# def mani(hi,name="kishore"):
#     print("my name is " + name )
# mani("ename")
# def mani(name="mani"):
#     hi

def f1(*n):
    print("var-arg function")
f1()
f1(10)
f1(10,20)
f1(10.20,30)

#wriate a program on sum of numbers
def sum(*n):
 result=0
 for x in n:
    result=result+x
 print("the sum is:" ,result)
sum()
sum(1,2)
sum(1,2,3)
#by using both the positonal arguments and var-arg arguments(variable length arguments)
def sum(name,*n):
 result=0
 for x in n:
    result=result+x
 print("the sum by:",name ,result)
sum("mani")
sum("kishore" ,1,2)
sum("kiran",1,2,3)

def sum(*n,name):
 result=0
 for x in n:
    result=result+x
 print("the sum by:",name ,result)
sum(name="mani")
sum( 1,2,name="kishore")
sum(1,2,3,name="kiran")

def sum(*n,name):
    print(type("name"))
def function():
    print("hello")
function()
def functio(mani=10):
    print("mani" + mani)
print(function())

#recursion
def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results",tri_recursion(4))
def fact(c):
    if c==0:
        return 1
    else:
        return c*fact(c-1)
print(fact(4))
mylist = [1,7,7,7,3,9,9,9,7,9,10,0]
print(sorted(set([i for i in mylist if mylist.count(i)<2])))