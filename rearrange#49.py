def rearrange(word1, word2):
    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()
    return sorted(word1) == sorted(word2)

word1 = input("Enter a word: ")
word2 = input("Enter a word made from rearranging the following word: ")

print(rearrange(word1, word2))