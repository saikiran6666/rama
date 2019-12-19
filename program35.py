#write a program on square od dictionary values print only keys
def sqrkeys():
    d=dict()
    for i in range(1,21):
        d[i]=i**2
    for k in d:
        print(k)
sqrkeys()