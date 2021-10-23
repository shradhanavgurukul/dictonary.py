y={'bijender':45,'deepak':60,'param':20,'anjali':30,'roshini':50}
l=list(y.items())   
l.sort()
print('Ascending order is',l) 
l=list(y.items())
l.sort() 
print('Descending order is',l)


k=[-1,2,4,-8,-9,6,4]
i=0
b=[]
while i<len(k):
    j=k[i]
    if j>0:
        b.append(0)
    elif j<0:
        b.append(i)
    i=i+1
print(b)




