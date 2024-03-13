from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def generate_des_key():
    # Generates a random DES key of 8 bytes (56 bits)
    return get_random_bytes(8)

def des_encrypt(message, key):
    # Creates a DES Cipher object with the key and encryption mode
    cipher = DES.new(key, DES.MODE_ECB)
    # Adds padding to the message
    padded_message = pad(message.encode('utf-8'), DES.block_size)
    # Encrypts the message
    encrypted_message = cipher.encrypt(padded_message)
    return encrypted_message

def des_decrypt(ciphertext, key):
    # Creates a DES Cipher object with the key and decryption mode
    cipher = DES.new(key, DES.MODE_ECB)
    # Decrypts the message
    decrypted_message = cipher.decrypt(ciphertext)
    # Removes padding from the decrypted message
    unpadded_message = unpad(decrypted_message, DES.block_size)
    return unpadded_message.decode('utf-8')

# Usage Example

while True:
    choice = input("What do you want to do, encrypt or decrypt? (c / d): ")
    if choice == 'c':
        message = input("Hello, enter the message to encrypt: ")
        key = generate_des_key()
        encrypted_message = des_encrypt(message, key)
        print(f"Encrypted Message: {encrypted_message}")
        break
    elif choice == 'd':
        message = input("Hello, enter the encrypted message: ")
        key = input("Enter the key: ")
        decrypted_message = des_decrypt(message, key)
        print(f"Decrypted Message: {decrypted_message}")
        break
    else:
        print("Invalid choice")
