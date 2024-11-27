5.# Check if two strings are anagrams ir not 
st1="listen"# anagrams are words that use same letters in same quantity but may be in different order
st2="silent"
out1=st1.replace(" ","")
out2=st2.replace(" ","")
if sorted(out1)==sorted(out2):
    print(" anagrams") # for the anagrmas we will be checking sorted
else:
    print("not anagrams ")    