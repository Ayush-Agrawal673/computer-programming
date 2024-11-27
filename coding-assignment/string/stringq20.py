20.# calculate the sum of divgits in a string 
str1="pynative12345"
total=0
for char in str1:
    if char.isdigit():
        total+=int(char)
print("The sum of digits in string",total)