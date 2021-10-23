students={'Aex':{'class':'v',
'rolld_id':2},
'puja':{'class':'v',
'roll_id':3}}
for a in students:
    print(a)
    for b in students[a]:
        print(b,':',students[a][b])





list1=["class-v","class-vi","class-vii","class-viii"]
list2=[1,2,2,3]
b=0
k={}
for i in list1:
    k[i]={list2[b]}
    b=b+1
print(k)
a=[1,2,3,4,5]
b={}
for i in a[::-1]:
    b={i:b}
print(b)


