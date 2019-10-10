#dictionary example
thisdict={
    "brand":"ford",
    "model":"mustang",
    "year":"1964"
}
print(thisdict)

#accessing items
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["year"]
print(x)
# get() method
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.get("brand")
print(x)
#change values by using key name
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict["year"] = 2019
print(thisdict)

#for loop through dictionary
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
      print(x)

#vlues one by one
      thisdict = {
          "brand": "Ford",
          "model": "Mustang",
          "year": 1964
      }
      for x in thisdict:
          print(thisdict[x])

# values() function to return the values
      thisdict = {
              "brand": "Ford",
              "model": "Mustang",
              "year": 1964
          }
for x in thisdict.values():
     print(x)

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x , y in thisdict.items():
  print(x, y)

#check if
  thisdict = {
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
  }
  if "brand" in thisdict:
      print("Yes, 'brand' is one of the keys in the thisdict dictionary")

# len() to determine how many items(key-valuess) in this dictionary
      thisdict = {
          "brand": "Ford",
          "model": "Mustang",
          "year": 1964
      }
      print(len(thisdict))

#adding items
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

#pop() removes the specified item with key
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("brand")
print(thisdict)

#popitem()  removes the last item
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

#del keyword
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["year"]
print(thisdict)

#clear() keyword
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)

#copy() method
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.copy()
print(x)

#dict()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

# nested dictionary
myfamily={
    "chaild1": {
        "name":"kiran",
        "age":21
    },
    "chaild2": {
        "name":"balaji",
        "age": 14
    },
    "chaild3": {
        "name":"satya",
        "age": 12
    }
}
print(myfamily)

#another way to nested dictionary
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily)

thisdict = dict(brand="Ford", model="Mustang", year=1964)
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
print(thisdict)



























