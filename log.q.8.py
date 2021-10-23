students_list={'S001':['math','science'],'S002':['math','science']}
print("orignal dictonary:",students_list)
students_dict={x.translate({32:None}):y for x,y in students_list.items()}
print("new dictonary:",students_dict)