import random
import string

chars = string.punctuation + string.ascii_letters + string.digits + " "

chars = list(chars)

keys = chars.copy()
random.shuffle(keys)

#encrypt
plain_text = input("Enter the text you want to encrypt : ")
cryptic_text = ""

for letter in plain_text:
    index=chars.index(letter)
    cryptic_text += keys[index]

print(f"Original message  : {plain_text}")
print(f"Encrypted message : {cryptic_text}")

#decrypt
cryptic_text = input("Enter the text you want to decrypt : ")
plain_text = ""

for letter in cryptic_text:
    index=keys.index(letter)
    plain_text += chars[index]


print(f"Encrypted message : {cryptic_text}")
print(f"Original message  : {plain_text}")