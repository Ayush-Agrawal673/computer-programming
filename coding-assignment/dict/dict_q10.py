# write a program find the frequencies of each word in a list and then create a dictionary 
def word_dictionary(word_list):
    freq_dict={}
    for word in word_list:
        freq_dict[word]=freq_dict.get(word,0)+1
        return freq_dict
words=["apple","banana","orange","cherry","papaya"]
print(word_dictionary(words))