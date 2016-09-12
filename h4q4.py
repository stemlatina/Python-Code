# Marilu D

#UserInput
word1 = input("Enter a word: ")
word2 = word1.lower()

#List
vowel_count1 = 0
con_count = 0

#For Loop
for ch in word2:
    if(ch == 'a' or ch == 'e' or ch == 'i' or ch =='o' or ch == 'u' or ch == 'y'):
        vowel_count1 += 1
    else:
        con_count += 1
print(word1,"has",vowel_count1,"Vowels and",con_count,"consonants.")
