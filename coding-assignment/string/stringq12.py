12.# fing the most frequent word in string
st=str(input())
a=st.split()
frequent_character=""
for i in a:
    a.count(i)
    if a.count(i)>a.count(frequent_character):
        frequent_character=i
print(frequent_character)        
