#problem2 part a

char = input("Enter a character:")
if(char.islower()):
    print(char,"is a lower case letter.")
elif(char.isupper()):
    print(char,"is an upper case letter.")
elif(char.isdigit()):
    print(char,"is a digit.")
else:
    print(char,"is a non-alphanumeric character.")

#problem2 part b

char = input("Enter a character:")
if(char >= 'A' and char <= 'Z'):
    print(char, "is an upper case letter.")
elif(char >= '0' and char <= '9'):
    print(char, "is a digit.")
elif(char >= 'a' and char <= 'z'):
    print(char,"is a lower case letter.")
else:
    print(char,"is a non-alphanumeric character.")
