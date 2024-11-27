#Check if a string has all unique characters
def has_unique_chars(s):
    return len(s) == len(set(s))

print("Has Unique Characters:", has_unique_chars("abcdef"))
