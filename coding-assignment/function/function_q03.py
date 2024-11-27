# a function to check whether two strings are anagrams or not 
def  is_anagram(str1,str2):
    return sorted(str1) ==  sorted(str2)
print("Is Anagram:",is_anagram('listen','silent'))