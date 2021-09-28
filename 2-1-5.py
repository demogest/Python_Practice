def prime(n):
    visit = [True for i in range(n+1)]
    s=[]
    for i in range(2,n+1):
        if visit[i]:
            s.append(i)
        for j in s:
            if i*j > n:
                break
            visit[i*j] = False
            if i%j == 0:
                break
    return s
def calc(n,s,pr):
    if n == 1:
        ans=""
        for i in s[1:]:
            ans=ans+"*"+str(i)
        print(str(s[0])+"="+ans[1:])
        return
    else:
        for i in pr:
            if n % i == 0:
                s.append(i)
                calc(n/i,s,pr)
                s.pop()
                break
n=eval(input())
s=list()
pr = []
s.append(n)
pr = prime(n)
calc(n,s,pr)
