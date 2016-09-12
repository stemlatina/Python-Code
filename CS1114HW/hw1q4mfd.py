# Marilu D


#program that takes years as input and prints out an estimated pop.


#define some useful constants
birthsPerSeconds = 7
deathsPerSecond = 13
newImmigrantsPerSecond = 35
currentPop = 307357870


#prompt user for input
years = int(input("Enter the number of years: "))

#math
birthsPerYear = int(60 * 60 * 24 * 365 / birthsPerSeconds)
deathsPerYear = int(60 * 60 * 24 * 365 / deathsPerSecond)
immigrantsPerYear = int(60 * 60 * 24 * 365 / newImmigrantsPerSecond)

#compute number of years/pop.
estimatedPop = currentPop + (birthsPerYear - deathsPerYear + immigrantsPerYear) * years

#print estimated pop
print("The Estimated population is = ", estimatedPop)

