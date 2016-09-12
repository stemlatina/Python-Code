#Marilu D

#User Input
dayJohn = int(input("Please enter the number of days John has worked: "))
hoursJohn = int(input("Please enter the number of hours John has worked: "))
minJohn = int(input("Please enter the number of minutes John has worked: "))
dayBill = int(input("Please enter the number of days Bill has worked: "))
hoursBill = int(input("Please enter the number of hours Bill has worked: "))
minBill = int(input("Please enter the number of minutes Bill has worked: "))


#Math
days1 = dayJohn + dayBill
hours1 = hoursJohn + hoursBill
mins1 = minJohn + minBill

totMin = (days1 * 24 * 60 ) +(hours1*60) + mins1

daysTotal = (totMin//60)//24

hours1 = (totMin//60)%24
minsTotal = totMin%60


#Results
print("The total time both of them worked together is: ",daysTotal,"days", hours1,"hours and",minsTotal,"minutes")
