n,s,a=1,0,2
def fib_Yield(n):
    a,b=0,1
    while n>0:
        yield b
        a,b=b,a+b
        n-=1
la = list(fib_Yield(21))
n=1
while n<=20:
    if n<20:
        print(str(a)+"/"+str(la[n])+"+",end="")
    else:
        print(str(a)+"/"+str(la[n]))
    s=a/la[n]
    a=a+la[n]
    n+=1
print(s)
