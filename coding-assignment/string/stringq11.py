11.# compressing the string using counts of repeated characher
st=str(input())
reg=""
for i in st:
    if i not in reg:
        a=st.count(i)
        print(f"{i}{a}", end="")
        reg+=i
