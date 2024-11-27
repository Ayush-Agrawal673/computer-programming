8.# code to count frequency of each character 
st="sohellamukherjee"

ch=""
for i in sorted(st):
    if i  not in ch:
        print(f"{i}:{st.count(i)}")