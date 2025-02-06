"""to check whether the word is palindrome or not"""

input = "madam"

""" if input = output then its true"""

output = input[::-1]
if input == output:
    print("yes the word is palindrome")
else:
    print("no the word is not palindrome")

