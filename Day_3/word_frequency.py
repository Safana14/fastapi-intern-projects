def count_words(text):
    words = text.lower().split()
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
        return frequency
sentence = input("Enter a sentence: ")
result = count_words(sentence)
print(result)