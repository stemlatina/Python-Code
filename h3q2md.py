#Marilu D

#User input
iteam1 = float(input("Please enter price of your first iteam: "))
iteam2 = float(input("Please enter price of your second iteam:  "))
cardHolder = input("Do you have club membership? (Y or N): ")
taxRate = float(input("Enter tax rate,e.g: 5.5 for %5.5 tax: "))

#Original Price
basePrice = iteam1+iteam2
print("Base Price =", basePrice)


#Price Calculations
if (iteam1 < iteam2): #If Iteam1 is less than iteam2 then iteam1 is half off
    iteam1 = iteam1 / 2
else: #Otherwise iteam2 is half off
    iteam2 = iteam2 / 2

priceBeforeDiscount = iteam1 + iteam2

#If user has a card then they get 10% off discount
if (cardHolder == 'Y' or cardHolder == 'y'):
    priceAfterDiscount = 0.9 * priceBeforeDiscount
else: #If they dont then they get no discount
    priceAfterDiscount = priceBeforeDiscount
#Print the $
print("Price after discounts =", priceAfterDiscount)
#Adding the tax
taxedPrice = (1 + taxRate/100)*priceAfterDiscount
print("Total price =", round(taxedPrice,2))

    


