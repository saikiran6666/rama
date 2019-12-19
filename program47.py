#write a program on even numbers in given list with in the range by using range function
def evnum():
    even=list(filter(lambda x:x%2==0,range(1,21)))
    return even
print(evnum())