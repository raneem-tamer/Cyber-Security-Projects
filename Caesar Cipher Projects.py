   #Caesar Cipher
#   A   B   C  D  E  F  G  H  I  J   K   L    M   N   O   P   Q   R   S   T   U   V   W   X   Y   Z
#   1   2   3  4  5  6  7  8  9  10  11  12   13  14  15  16  17  18  19  20  21  22  23  24  25  26

#Encrypt                                  | Decrypt
#Equation = [ Letter + key ] % 26         |Equation = [ Letter - key ] % 26
# Cyber Security   = DZCFS TFDVSJUZ       | DZCFS TFDVSJUZ  =  Cyber Security
#Cyber       Key = 1  Cipher = DZCFS      | DZCFS
#C = 3+1=  4                   D          | D = 4-1 = 3             C
#y = 25+1= 26                  Z          | Z = 26-1 = 25           y
#b = 2+1= 3                    C          | C = 3-1 = 2             b
#e = 5+1= 6                    F          | F = 6-1 = 5             e
#r = 18+1= 19                  S          | S = 19-1 = 18           r
#Security    Key = 1   Cipher = TFDVSJUZ  |TFDVSJUZ
#S = 19+1 =20                  T          | T = 20-1 = 19           S
#e = 5+1 = 6                   F          | F = 6-1 = 5             e
#c = 3+1 = 4                   D          | D = 4-1 = 3             c
#u = 21+1 = 22                 V          | V = 22-1 = 21           u
#r = 18+1 = 19                 S          | S = 19-1 = 18           r
#i = 9+1 = 10                  J          | J = 10-1 = 9            i
#t = 20+1 = 21                 U          | U = 21-1= 20            t
#y = 25+1 = 26                 Z          | Z = 26-1 = 25           y

def encrypt(text, key):
    cipher_list = []
    for char in text:
        if char.isalpha():  # Only encrypt alphabetic characters
            shift = key % 26
            if char.islower():
                new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            cipher_list.append(new_char)
        else:
            cipher_list.append(char)  # Keep non-alphabetic characters unchanged
    return ''.join(cipher_list)

def decrypt(text, key):
    decipher_list = []
    for char in text:
        if char.isalpha():  # Only decrypt alphabetic characters
            shift = key % 26
            if char.islower():
                new_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            else:
                new_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            decipher_list.append(new_char)
        else:
            decipher_list.append(char)  # Keep non-alphabetic characters unchanged
    return ''.join(decipher_list)

print("Starting the script...")

# Encryption part
text_to_encrypt = input("Enter the text to encrypt: ")
print(f"Text to encrypt: {text_to_encrypt}")
key = int(input("Enter the encryption key: "))
print(f"Encryption key: {key}")

encrypted_text = encrypt(text_to_encrypt, key)
print(f"Encrypted text: {encrypted_text}")

# Decryption part
print("\nStarting the decryption...")
text_to_decrypt = encrypted_text  # Use the previously encrypted text
print(f"Text to decrypt: {text_to_decrypt}")
decryption_key = key  # Use the same key for decryption
print(f"Decryption key: {decryption_key}")

decrypted_text = decrypt(text_to_decrypt, decryption_key)
print(f"Decrypted text: {decrypted_text}")
