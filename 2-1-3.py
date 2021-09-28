a, n = eval(input())
s = ""
while n>1:
    s=s+str(a)+"+"
    a=a*10+int(str(a)[-1])
    n-=1
s=s+str(a)
print(s)
print(eval(s))
