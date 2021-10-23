my_dict="w3resource"
a=[]
for i in my_dict:
    if i not in a:
        a.append(i)
for i in range(0,len(a)):
    count=0
    for j in range(0,len(my_dict)):
        if a[i]==my_dict[j]:
            count+=1
    print(a[i],"=",count)


      


