def encrypt(msg,shift):
    result = ""
    for i in msg:
        result += chr(ord(i) + shift)
    return result

def decrypt(msg,shift):
    result = ""
    for i in msg:
        result += chr(ord(i) - shift)
    return result

loop = True
while loop:
    choice = int(input("Enter '0' to encrypt or '1' to decrypt:"))
    if choice == 0:
        text = input("Enter text to encrypt: ")
        shift = int(input("Enter shift number (left shift -> negative number, right shift -> positive number) : "))
        print(encrypt(text, shift))
        loop = False
    elif choice == 1:
        text = input("Enter text to decrypt: ")
        shift = int(input("Enter shift number (left shift -> negative number, right shift -> positive number) : "))
        print(decrypt(text, shift))
        loop = False

