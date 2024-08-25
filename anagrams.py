 # working with anagrams
def are_anagrams(text1, text2):
    # removing spaces and conversion of texts into lowercase
    cleaned_text1 = ''.join(text1.lower().split())
    cleaned_text2 = ''.join(text2.lower().split())

    # character sorting and comparison
    return sorted(cleaned_text1) == sorted(cleaned_text2)

# asking the input from the user
text1 = input('Enter a string: ')
text2 = input('Enter another string: ')

# checking if hey are anagrams
if text1 and text2:
    if are_anagrams(text1, text2):
        print("They are anagrams")

    else:
        print("They are not anagrams")
else:
    print("Empty strings are not anagrams. ")





