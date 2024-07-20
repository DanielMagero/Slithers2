#2
def count_char(chat):
    #make a dictionary
    dic_count = {}
    for char in chat:
        if char in dic_count:
            dic_count[char] += 1
        else:
            dic_count[char] = 1
    return dic_count

string = input("Enter a word of your choice:")
str_count = count_char(string)
print(str_count)




#4
def swap(str1, str2):
    #pick the last values of the string after the string in position 2 and then add the first letters of the other

    str1_new = str1[:2] + str2[2:]
    str2_new = str2[:2] + str1[2:]

    final_str = str1_new + " " + str2_new
    return final_str

print("Enter two words that are more than three letter long.")
str1 = input("Enter your first word: ")
str2 = input("Enter your second word:")

final_str = swap(str1, str2)

print(final_str)





#7
def omit(str1):
    #join letters together with no space
    #check the position and whether it's an even number
    
    final_str = ''.join([char for index, char in enumerate(str1) if index % 2 == 0])
    return final_str

print("Removing odd positioned letters from a word.")
str1 = input("Enter a word of your choice:")
print(omit(str1))





#10
def str_rev(m):
    #reverse the arrangement of the string
    new_str = m[::-1]
    return new_str

m = input("Word reversal!! \nEnter a word of your choice:")
print(str_rev(m))




#12
def rev_word(str1):
    #split the sentence into individual words
    words = str1.split()

    #reverse them
    rev_words = words[::-1]
    words2 = ' '.join(rev_words)
    return words2

str1 = input("Enter a sentence of your choice:")
print(rev_word(str1))





#13
def vowel_count(chat):
    #create a set of the vowels accounting for upper and lower case
    vowels = set("aeiouAEIOU")
    #create a set for where the discovered vowels will be stored
    the_vowels = set()
    #initialize the variable to be used to tally
    total_vow = 0

    for char in chat:
        if char in vowels:
            #add any new found vowels to the set without repetition
            the_vowels.add(char)

            total_vow += 1

    the_vowels_list = sorted(the_vowels)

    if total_vow > 0:
        print("Vowels in the word are:", ' '.join(the_vowels_list))
        print("The total number of vowels is:", total_vow)
    else:
        print("No vowels found.")
    return the_vowels, total_vow

chat = input("Enter a word of your choice:")

the_vowels, total_vow = vowel_count(chat)




#16
def digit_sum(str):
    #initialize variable
    sum_dig = 0
    for char in str:
        #count only numeric characters
        if char.isdigit():
            sum_dig += int(char)
    return sum_dig

str = input("Enter a string with numbers in it: ")
print(digit_sum(str))




#18
def chartype_count(str):
    #initialize variables for all types of characters
    lower_case = 0
    upper_case = 0
    spec_char = 0
    num_char = 0

    for char in str:
        #count for each
        if char.islower():
            lower_case += 1
        elif char.isupper():
            upper_case += 1
        elif char.isdigit():
            num_char += 1
        else:
            spec_char += 1
    
    #returning a tuple
    return lower_case, upper_case, spec_char, num_char

str = input("Enter a string containing different types of characters: ")
lower_case, upper_case, spec_char, num_char = chartype_count(str)
print(f"Lowercase: {lower_case} \nUppercase: {upper_case} \nSpecial characters: {spec_char} \nNumeric characters: {num_char}")




#45
def titlecase(str):
    #converting string to title format
    return str.title()

str = input("Enter a phrase of your choice: ")
print(titlecase(str))



#49
def rearrange(word1, word2):

    #convert both words to lowercase for case sensitivity
    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()

    #check that both sets have exactly the same letters
    return sorted(word1) == sorted(word2)

word1 = input("Enter a word: ")
word2 = input("Enter a word made from rearranging the following word: ")

print(rearrange(word1, word2))