thisset = {"apple", "banana", "cherry"}
print(thisset)

#access items using for loop
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

# check banana in this set
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

# add items to set using add() method
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

# add multiple items to set using update() method
thisset = {"apple", "banana", "cherry"}
thisset.update(["orange", "mango", "grapes"])
print(thisset)

 #no of items in a set using len() method
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

# remove items by using remove method
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

# remove an item in set by using discard() method
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

# to remove item from set using pop() method
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

# to clear the all items in set by using cleara() method
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

#thisset = {"apple", "banana", "cherry"}
#del thisset
#print(thisset)

# set constructor
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)