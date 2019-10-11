#tuple example
thistuple=("apple","banana","cherry")
print(thistuple)

#access tuple items
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#loop through a tuple
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
#check if items exists
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

# tuple length
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#tuple constractor
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)