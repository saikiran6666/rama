#example for generators
def mygen():
    n=1
    print("this is printed first")
    yield n
    n+=1
    print("this is the second")
    yield n
    n+=1
    print("this is printed at last")
    yield n
a=mygen()
next(a)
next(a)
next(a)
# by using for loop iterate the items
def mygen():
    n=1
    print("this is printed first")
    yield n
    n+=1
    print("this is the second")
    yield n
    n+=1
    print("this is printed at last")
    yield n
for items in mygen():
    print(items)


def simplegen():
    yield 1
    yield 2
    yield 3
for value in simplegen():
  print(value)

#reverse string by using loop with generator yeild
def strgrev(mystrg):
    lt=len(mystrg)
    for i in range(lt -1,-1,-1):
        yield mystrg[i]
for char in strgrev("manikishore"):
    print(char)

# python generator expression
mylist=[1,3,6,10]
[x**2 for x in mylist]
(x**2 for x in mylist)


mylist=[1,3,6,10]
a=(x**2 for x in mylist)
print(next(a))
print(next(a))
print(next(a))
print(next(a))

def powtow(max=0):
    n=0
    while n<max:
        yield 2**n
        n+=1
a=powtow()
print(next(a))
print(next(a))
print(next(a))
#represent infinite stream
def alleven():
    n=0
    while True:
        yield n
        n+=2
a=alleven()
print(next(a))
print(next(a))
print(next(a))
print(next(a))


# A simple generator for Fibonacci Numbers
def fib(limit):
    # Initialize first two Fibonacci Numbers
    a, b = 0, 1

    # One by one yield next Fibonacci Number
    while a < limit:
        yield a
        a, b = b, a + b

    # Create a generator object


x = fib(5)

# Iterating over the generator object using next
print(x.next());  # In Python 3, __next__()
print(x.next());
print(x.next());
print(x.next());
print(x.next());

# Iterating over the generator object using for
# in loop.
print("\nUsing for in loop")
for i in fib(5):
    print(i)




