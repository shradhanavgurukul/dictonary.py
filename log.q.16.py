# list1=["a","b","c","d"]
# list2=[1,2,3,4]
# b=0
# k={}
# for i in list1:
#     k[i]=list2[b]
#     b=b+1
# print(k)



k={"item1":45.50,"item2":35,"item3":41.30,"item4":55,"item5":24}
l=list(k.items())
l.sort() 
print('Descending order is',l)
