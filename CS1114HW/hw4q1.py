string = input("Enter a string:")
mid_string = len(string)//2
mid_character = string[mid_string]

print("Middle character:", mid_character)
first_half = string[0:mid_string]
second_half = string[mid_string+1:]
print("First half:",first_half)
print("Second half:",second_half)
