10.# check if two strings are rotations of each other 
st=str(input())
st1=str(input())
if len(st)==len(st1)and st1 in st+st:
    print(True)
else:
    print(False)   