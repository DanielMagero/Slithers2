def vowel_count(chat):
    vowels = set("aeiouAEIOU")
    the_vowels = set()
    total_vow = 0

    for char in chat:
        if char in vowels:
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
    
