#Opening the file using open() and reading contents using read()
file = open("textfile.txt", "r")
content = file.read()
print(content)

num_words = 0
num_charc = 0
norepeatset = set()  

for line in content.splitlines():
    words = line.split()
    num_words += len(words)
    for c in line:  
        if c != ' ':  
            if c not in norepeatset:  # Check if the character is already processed
                norepeatset.add(c)  
                print(f"The ASCII value of '{c}' is", ord(c))
            num_charc += 1

print("Number of words: ", num_words)
print("Number of characters : ", num_charc)
print("Number of unique characters: ", len(norepeatset))
file.close()