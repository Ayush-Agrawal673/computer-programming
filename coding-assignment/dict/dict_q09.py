# write a program to find key with maximum value 
def max_value(d):
    return max(d, key=d.get)
my_dict={"apple":10,"banana":20,"cherry":5}
print(max_value(my_dict))