# write a program to find intersection of two dictionaries
def intersection(dict1,dict2):
    return {key:dict1[key] for key in dict1 if key in dict2 }
dict1={"a":1,"b":2,"c":3}
dict2={"b":2,"c":4,"d":5}
print(intersection(dict1,dict2))