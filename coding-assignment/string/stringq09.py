9.# find the first non repeating character present in a string 
st="swiss"
for i in st:
    A=st.count(i)
    if A==1:
        print(i)
        break