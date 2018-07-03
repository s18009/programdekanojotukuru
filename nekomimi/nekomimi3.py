word = input()
count = 0
for i in range(len(word)):
    if word[i:i+3] == "cat":
        count += 1
print(count)
