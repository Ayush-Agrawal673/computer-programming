 #Reverse words in a sentence
def reverse_words(sentence):
    return " ".join(sentence.split()[::-1])

print("Reversed Words:", reverse_words("Hello world this is Python"))