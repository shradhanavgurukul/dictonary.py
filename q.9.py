n="MISSISSIPPI"
a=[]
for i in n:
    if i not in a:
        a.append(i)
for i in range(0,len(a)):
    count=0
    for j in range(0,len(n)):
        if a[i]==n[j]:
            count+=1
    print(a[i],"=",count)



    