6.#Replace list’s item with new value if found
#You have given a Python list. Write a program to find value 10 in the list, 
# and if it is present, replace it with 200. Only update the first occurrence of an item.
list=[5, 20, 15, 10, 25, 50, 10]
index=list.index(10)
list[index]=200
print(list)
