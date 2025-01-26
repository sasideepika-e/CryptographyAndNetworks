#Monoalphabetic Cipher Encryption
key = "ANDREWICKSOHTBFGJLMPQUVXYZ"
plain_text = "wewishtoreplaceplayer".upper()
encrypted_text = ""

for char in plain_text:
    encrypted_text += key[ord(char) - ord('A')]

print("Encrypted Text:", encrypted_text)