# Write a function to check if a given string is a palindrome
# (reads the same backward as forward).

def palindrome_check(s):
    s = " ".join(filter(str.isalnum, s)).lower()
    return s == s[:: -1]


input_string = input("Enter a string: ")
if palindrome_check(input_string):
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")
