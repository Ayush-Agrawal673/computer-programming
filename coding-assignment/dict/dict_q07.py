# write a program to update dictionary with another dictionary 
def update(dict1,dict2):
    dict1.update(dict2)
    return dict1
dict1={"a":5,"b":2}
dict2={"b":4,"c":2}
print(update(dict1,dict2))
