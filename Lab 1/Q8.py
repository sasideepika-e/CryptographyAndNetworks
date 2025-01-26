#Playfair Cipher Decryption
def find_position(matrix, char):
    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            if col == char:
                return i, j

def playfair_decrypt(text, matrix):
    result = ""
    i = 0
    while i < len(text):
        char1 = text[i]
        char2 = text[i+1] if i+1 < len(text) else 'x'
        pos1 = find_position(matrix, char1)
        pos2 = find_position(matrix, char2)
        if pos1[0] == pos2[0]:
            result += matrix[pos1[0]][(pos1[1]-1) % 5]
            result += matrix[pos2[0]][(pos2[1]-1) % 5]
        elif pos1[1] == pos2[1]:
            result += matrix[(pos1[0]-1) % 5][pos1[1]]
            result += matrix[(pos2[0]-1) % 5][pos2[1]]
        else:
            result += matrix[pos1[0]][pos2[1]]
            result += matrix[pos2[0]][pos1[1]]
        i += 2
    return result

cipher_text = "LIIUDLTQNSLIZETQVTPKZEZFVBVZ".lower()
key_matrix = [
    ['s', 'r', 'm', 'a', 'p'],
    ['u', 'n', 'i', 'v', 'e'],
    ['t', 'y', 'b', 'c', 'd'],
    ['f', 'g', 'h', 'k', 'l'],
    ['o', 'q', 'w', 'x', 'z']
]

decrypted_text = playfair_decrypt(cipher_text, key_matrix)
print("Decrypted Text:", decrypted_text)