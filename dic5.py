name = input()
if name[-4:] != '.txt':
    name += '.txt'
txt = open(name,encoding='utf-8').read()
fre = {}
for ch in txt:
    if '\u4e00' <= ch <= '\u9fa5':
        if ch in fre:
            fre[ch]+=1
        else:
            fre[ch]=1

for k,v in fre.items():
    print('{}:{}'.format(k,v))
