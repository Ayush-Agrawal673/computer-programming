# write a function to find longest word in a string 
def longest_word(s):
    words=s.split()
    return max(words,key=len)
print("longest word",longest_word("The quick brown fox jump over the lazy dog "))