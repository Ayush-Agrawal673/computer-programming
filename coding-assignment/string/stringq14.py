14.# write a program to get string made of forst 2 and last two characteres of given string
st="w3resouce"
first_two=st[0]+st[1]
a=len(st)-1
b=a-1
last_two=st[b]+st[a]
required_string=first_two+last_two
print(required_string)