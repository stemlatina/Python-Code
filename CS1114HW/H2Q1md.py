#Marilu Duque
#Program A

#User Input
userNum1 = int(input("Please enter weight in kilograms: "))
userNum2 = float(input("Please enter height in meters: "))

#math
BMI = userNum1/userNum2**2


#Results
print("BMI is: ",BMI,)


#Program B
userNum3 = int(input("lease enter weight in pounds: "))
userNum4 = int(input("Please enter height in inches: "))


#math
num3Metric = userNum3 * 0.453592
num4Metric = userNum4 * 0.0254
BMI2 = num3Metric/num4Metric**2


#Results
print("BMI is: ",BMI2,)

