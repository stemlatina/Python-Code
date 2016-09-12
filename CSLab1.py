#CS Lab 1

#1
#Prints my name
print ("Marilu")

#2
#2 Asks user for input and prints out sum diff and product
int1 = int(input("Please enter an integer: "))
int2 = int(input("Please enter an integer: "))
difference = int1 - int2
sum1 = int1 + int2
product = int1 * int2 

print ("The sum is: " ,sum1)
print("The diff. is: " ,difference)
print("The product is: " ,product)


#3
#Fahrenheit to Celsius and backwards

fahDegree1 = int(input("Please enter a Fahrenheit temperature: "))
celsius = (fahDegree1 - 32) * 5/9
print (" In Celsius it is: " ,celsius, "In Fahrenheit it is: ",fahDegree1,)
