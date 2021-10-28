#使用列表生成式创建列表，列表的元素依次为,0,1,8,27.
li = [x**3 for x in range(4)]
li.append(li.pop(0))
for i in li[:-1]:
    print(i,end=',')
print(li[-1])
