6.# find longest word iin string 
st1="The quick brown fox"
out=st1.split()
longest_word=""
for i in out:
    if len(i)> len(longest_word):
        longest_word=i
print(longest_word)    