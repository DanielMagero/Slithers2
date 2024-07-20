def rev_word(str1):
    words = str1.split()
    rev_words = words[::-1]
    words2 = ' '.join(rev_words)
    return words2

str1 = input("Enter a sentence of your choice:")
print(rev_word(str1))