# Marilu D

#User Input Part A
charac1 = input("Enter a character:")

#Ifstatements
if(charac1.islower()):
    print(charac1,"is a lower case letter. ")
      #Elif
elif(charac1.isupper()):
    print(charac1,"is an upper case letter. ")
elif(charac1.isdigit()):
    print(charac1,"is a digit. ")
#Else 
else:
    print(charac1,"is a non-alphanumeric character. ")


#User Input Part B
charac2 = input("Enter a character: ")

#Ifstatements
if(charac2 >= 'A' and charac2 <= 'Z'):
    print(charac2, "is an upper case letter. ")
    #Elif
elif(charac2 >= '0' and charac2 <= '9'):
    print(char, "is a digit.")
elif(charac2 >= 'a' and charac2 <= 'z'):
    print(charac2,"is a lower case letter. ")
#Else 
else:
    print(charac2,"is a non-alphanumeric character. ")
