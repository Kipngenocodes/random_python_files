# the program will check whether it is palindrome or not

def is_palindrome(text):
    # removing space in a text provided
    cleaned_text = ''.join(text.lower().split())
    # checking if the cleaned_text is the same forwards and backwards
    return cleaned_text == cleaned_text[::-1]

#taking the user input
user_input = input("Enter a Text: ")

# checking if it is a palindrome
if user_input:
    if is_palindrome(user_input):
        print(f"{user_input} is a palindrome")

    else:
        print(f"{user_input} is not a palindrome")
else:
    print(f"{user_input} is an empty string")
