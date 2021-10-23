my_dict = {

    'a':50, 

    'b':58, 

    'c':56,

    'd':40, 

    'e':100, 

    'f':20

    }
a=[]
for i in my_dict.keys():
    a.append(i)
    for j in my_dict.values():
        a.append(j)
i=0
while i<len(a):
    j=0
    while j<len(a)-1:
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
        j=j+1
    i=i+1
k=(a[-3:])
print(k)

