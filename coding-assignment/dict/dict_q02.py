# remove all keys with value less than 10 from the dictionary
def remove(d):
    return{key:value for key,value in d.items() if value>=10}
my_dict={"apple": 5, "banana":15 , "cherry":8}
print(remove(my_dict))