dic={"a":1,"b":2,"c":3,"d":4}
a=[]
b=[]
for i in dic:
    a.append(i)
    b.append(dic[i])
print(a)
print(b)

i=1
a=[]
while i<len(dic):
    a.append(i)
    i=i+1
print(a)
