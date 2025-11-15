"""
Q: Write a Python program to check whether two strings are anagrams.
   Two strings are anagrams if they contain the same characters
   in the same frequency, even if the order is different.

Example:
    Input:  "listen", "silent"
    Output: True
"""

word_1 = input("Enter the first word: ")
word_2 = input("Enter the second word: ")

# Convert to lowercase
word_1 = word_1.lower()
word_2 = word_2.lower()

# Check if the sorted words are equal
if sorted(word_1) == sorted(word_2):
    print(True)
else:
    print(False)
