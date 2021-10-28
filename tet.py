s=input('')
sa = ''
for i in s:
     sa+=chr((ord(i)+3-ord('a')) % 26 + ord('a'))
print(sa)
