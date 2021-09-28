from functools import reduce
x,y=2,1
l = []
s=str(x)+"/"+str(y)+"+"
l.append(x/y)
for i in range(19):
    x,y=x+y,x
    s=s+str(x)+"/"+str(y)+"+"
    l.append(x/y)
print(s[:-1])
print(reduce(lambda x,y:x+y,l))