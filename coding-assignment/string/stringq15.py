15.# write a python program to reverse words in a string 
st="The quick brown fox"
for line in st.split("\n"):
    print(" ".join(line.split()[::-1]))