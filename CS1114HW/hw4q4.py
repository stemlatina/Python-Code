word = input("Enter a word:")
word1 = word.lower()
vowel_count = 0
con_count = 0
for ch in word1:
    if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or ch == 'y'):
        vowel_count = vowel_count + 1
    else:
        con_count = con_count + 1
print(word,"has",vowel_count,"vowels and",con_count,"consonants.")
