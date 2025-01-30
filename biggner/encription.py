import random
import string

# Generate character set
char = list(string.punctuation + string.digits + string.ascii_letters + string.ascii_uppercase + " ")
key = char.copy()
random.shuffle(key)  # Create a shuffled key mapping

# Encryption Function
def encryption():
    message = input("Enter the message to encrypt: ")
    secured = ""
    for letter in message:
        if letter in char: 
            new = char.index(letter)
            secured += key[new]
        else:
            secured += letter  
    print(f"\nOriginal Message: {message}")
    print(f"Encrypted Message: {secured}")

# Decryption Function
def decryption():
    dec = input("Enter the message to decrypt: ")
    dec_txt = ""
    for letter in dec:
        if letter in key:  
            nbr = key.index(letter)
            dec_txt += char[nbr]
        else:
            dec_txt += letter  
    print(f"\nDecrypted Message: {dec_txt}")

che = input("Enter what you want to do (encryption or decryption):\n").strip().lower()

if "encryption" in che:
    encryption()
elif "decryption" in che:
    decryption()
else:
    print("Invalid choice! Please enter either 'encryption' or 'decryption'.")
