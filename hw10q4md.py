#Marilu D
#Q4

#import
import decimal
def readMenu():
    '''reads the menu for the user'''
    num1 = int(input("How many items are on the menu?"))#user input
    menuList = []
    for i in range(num1):
        price = input("Enter the item in the form 'item:price': ")#user input
        tuple1 = (price.split(":")[0],round(float(num1.split(":")[1]),2))
        menuList.append(tuple1)
    return menuList#return the list

def read_customer_order():
    '''reads the order that user inputs'''
    done = True
    listOrder = []
    order = input("What would you like to order?")#user input
    listOrder.append(order)
    while done:
        order = input("What else would you like to order or type 'Done':")#user input
        if order.lower() == 'done':
            done = False
        else:
            listOrder.append(order)
        return listOrder

def computer_price(menuList,listOrder):
    '''uses the price in the loop'''
    total = 0
    for order in listOrder:#for loop for the order
        if order == item[0]:
            total += item[1]
    return total

def main():
    '''main def'''
    menu = readMenu()
    for i in range(3):
        order = read_customer_order()
        total = computer_price(menu,order)
        tax = total * 0.085
        tip = total * 0.15
        total += tax + tip
        print(round(total,2))
main()
