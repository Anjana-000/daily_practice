"Given a string
If the string contain vowels replace every character of the string with first occurring vowel, If the string does not contain a vowel return original string

For example
Input string : BOB
Output : OOO"

s=input()
fst_vowel=None
vowels=set('aeiuoAEIUO')
for i in s:
    if i in vowels:
        fst_vowel=i
        break
if fst_vowel!=None:
    print (fst_vowel*len(s))
else:
    print(s)
