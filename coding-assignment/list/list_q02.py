2.# concate two list index wise 
list1=["m","na","i","ay"]
list2=["y","me","s","ush"]
list3=[i+j for i,j in zip(list1,list2) ]
print(list3)