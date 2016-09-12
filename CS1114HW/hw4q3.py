math_exp = input("Enter a mathematical expression:")
first_space = math_exp.find(' ')
operand1 = ''

for ch in math_exp[0:first_space+1]:
    if(ch.isdigit()):
        operand1 = operand1 + ch
operand1 = int(operand1)

math_exp2 = math_exp[first_space:]
operand2 = ''

for ch2 in math_exp2:
    if(ch2.isdigit()):
        operand2 = operand2 + ch2
operand2 = int(operand2)

op = math_exp2[1]

if(op == '+'):
    ans = operand1 + operand2
    print(math_exp,"=", ans)
elif(op == '-'):
    ans = operand1 - operand2
    print(math_exp,"=",ans)
elif(op == '*'):
    ans = operand1*operand2
    print(math_exp,"=", ans)
elif(op == '/'):
    ans = operand1/operand2
    print(math_exp,"=",ans)

