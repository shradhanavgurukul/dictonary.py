dic={
    "ball":"red",
    "bat":4,
    "wickets":8,
    "ball":"green",
    "bat":3
}
a={}
for i,j in dic.items():
    j=i
    if i==j:
        a.update(dic)
        print(a)
        break

a={}
for i,j in dic.items():
    j=i
    if i==j:
        a.update(dic)
        print(a)
        break



    


















