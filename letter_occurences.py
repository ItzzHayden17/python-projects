letters = input("Please input your choice of letters: ")

letter_occurences ={}
for i in  letters:
    if i in letter_occurences:
        letter_occurences[i] += 1
    else:
        letter_occurences[i]=1

print(letter_occurences)