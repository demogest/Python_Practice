day = ['Mon','Tues','Wed','Thur','Fri','Sat','Sun']
ind = [i for i in range(1,8)]
dic1 = {}
s=''
for i,j in zip(day,ind):
    print('Key is:{},Value is:{}'.format(j,i))
    dic1[j] = i
    s += ',{}:{}'.format(j,i)
print(s[1:])
dic2 = {}
s=''
for i in dic1:
    print('Key is:{},Value is:{}'.format(dic1[i],i))
    dic2[dic1[i]]=i
    s += ',{}:{}'.format(dic1[i],i)
print(s[1:])
