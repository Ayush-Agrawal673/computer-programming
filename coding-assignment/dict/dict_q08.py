# write program to sort dictionary by values 
def sort(d):
    return dict(sorted(d.items(),key=lambda item:item[1]))
my_dict={"apple":10,"banana":5,"cherry":7}
print(sort(my_dict))