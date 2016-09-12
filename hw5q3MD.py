#Marilu D

#UserInput

user1 = input("Please enter a string of lowercase letters: ")
#DEF
count = 0
inc = True

#While Loop/ length of user1 input
while inc and count < len(user1)-1: #while length of user oneis true + count then...
    if ord(user1[count]) < ord(user1[count+1]): #alphabet increasing
        count += 1 #While loop end
    else:#else statement for false
        inc = False
if inc == True: #TrueResult
    print(user1,"is increasing.")
else:#false results
    print(user1,"is not increasing.")
#Program End
