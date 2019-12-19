#write aprogran in dictionary squarea of key values print only values
def sqrkeys():
    d=dict()
    for i in range(1,21):
        d[i]=i**2
    for (k,v) in d.items():
      print(v)
sqrkeys()


