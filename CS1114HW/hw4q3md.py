# Marilu D

#UserInput
mathexp = input("Enter a mathematical expression: ")
space1 = mathexp.find(' ')
operand1 = ''

#For loops1
for ch1 in mathexp[0:space1+1]:
    if(ch1.isdigit()):
        operand1 += ch1
operand1 = int(operand1)

mathexp2 = mathexp[space1:]
operand2 = ''

#For Loop2
for ch2 in mathexp2:
    if(ch2.isdigit()):
        operand2 += ch2
operand2 = int(operand2)
#Variable
op1 = mathexp2[1]
#Math/Results
if(op1 == '+'):
    ans = operand1 + operand2
    print(mathexp,"=", ans)
elif(op1 == '-'):
    ans = operand1 - operand2
    print(mathexp,"=",ans)
elif(op1 == '*'):
    ans = operand1*operand2
    print(mathexp,"=", ans)
elif(op1 == '/'):
    ans = operand1/operand2
    print(mathexp,"=",ans)
