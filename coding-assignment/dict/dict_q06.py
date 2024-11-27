# write a program to find the common key between two dictionaries 
def common(dict1,dict2):
    return list(dict1.keys() & dict2.keys())
dict1={"a":1,"b":2,"c":3}
dict2={"b":2,"c":4,"d":5}
print(common(dict1,dict2))