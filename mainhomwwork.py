# Check if the character is an alphabet

char = input("Enter a character: ")

if ('A' <= char <= 'Z') or ('a' <= char <= 'z'):
    print("It's an alphabet.")
else:
    print("It's not an alphabet.")
