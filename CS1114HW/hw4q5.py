password = input("Enter a password:")
upper_count = 0
lower_count = 0
digit_count = 0
spc_count = 0

if len(password) > 8 or len(password) == 8:
    for ch in password:
        if ch.isupper():
            upper_count = upper_count + 1
        elif ch.islower():
            lower_count = lower_count + 1
        elif ch.isdigit():
            digit_count = digit_count + 1
        elif ch == '!' or ch == '@' or ch == '#' or ch == '$':
            spc_count = spc_count + 1
if upper_count >= 2 and lower_count >= 1 and digit_count >= 2 and spc_count >= 1:
        print(password,"is a valid password.")
else:
    print(password,"is not a valid password.")

    
