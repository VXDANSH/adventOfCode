# sample = ['1abc2', 'pqr3fdskj8as', 'afd1asdf2dfd6asdf7asdf5sd', 'treb7uchet']

sample = []

with open("/Users/vedansh/Desktop/AdventOfCode/pz1.txt") as w:
    sample = w.readlines()

sum = 0

for s in sample:
    for j in s:
        if j.isdigit() == True:
            left_digit = int(j)
            sum += left_digit*10
            left_digit = 0
            break

    for j in s[::-1]:
        if j.isdigit() == True:
            right_digit = int(j)
            sum += right_digit
            right_digit = 0
            break

print(sum)