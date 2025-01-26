#Playfair Key Matrix Generation
key = "srmapuniversity".replace('j', 'i')
alphabet = "abcdefghiklmnopqrstuvwxyz"
matrix = []
used = set()

for char in key:
    if char not in used:
        matrix.append(char)
        used.add(char)

for char in alphabet:
    if char not in used:
        matrix.append(char)

key_matrix = [matrix[i:i+5] for i in range(0, len(matrix), 5)]

for row in key_matrix:
    print(" ".join(row))