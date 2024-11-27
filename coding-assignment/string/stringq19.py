19.# create a string made up of first last and middle character 
str1="james"
result=str1[0]
l=len(str1)
middle=int(l/2)
res=result+str1[middle]
res=res+ str1[l-1]
print(res)