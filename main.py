# This is a python program to test for a palindrome
word_Palindrome = input("Type in a palindrome word: ")

Palindrome_word = word_Palindrome[::-1]
print(Palindrome_word)

if Palindrome_word == word_Palindrome :
    print(word_Palindrome , " is a PALINDROME")

else:
    print(Palindrome_word , " is not a PALINDROME")
