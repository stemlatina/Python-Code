#Marilu D

#UserInput
textLine = input("Please enter a line of text: ")
remove = input("Please enter the character you want to remove: ")
stringSpace = ' ' #space def

#forloop
for char in textLine:
    if char != remove: #if statement != doesnt equal removew
        stringSpace += char #endloop
    else: #else for space
        stringSpace += ' ' 
print(stringSpace) #results


