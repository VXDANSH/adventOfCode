#Isolate each line as an array
#Check the 8 characters around each number for symbols
#If anything is a symbol (not a .), add the number to sum
#If number located to the left but not right, add to sum
#If number located to left and right, x10 and add to sum
#If number located to right but not left, check if number to right has numebrs to l and r
#If it does, multiply by 10^2 and add to sum, else multiply by 10 and add to sum
from termcolor import cprint

with open("d3input.txt") as file:
    data = file.readlines()

def getnumber(i, j):
    n = 0
    while data[i][j].isdigit() == True:
        n = n*10 + int(data[i][j])
        j += 1
    return n

def containsSymbol(row, start_col, end_col):
    for col in range(start_col, end_col):
        print('checking symbol at row: ' + str(row) + ' col : ' + str(col) + ' for symbol')
        if data[row][col].isdigit() == False and data[row][col] != '.':
            return True
    return False

def checksymbol(row, col, number):
        #check to the left 
        symbol_left = containsSymbol(row, max(col-1,0), col)
        if symbol_left == True:
            cprint('Symbol found on left', 'light_blue')

        #check to the right
        symbol_right = containsSymbol(row, col+len(str(number)), min(col+len(str(number))+1, len(data[row])))
        if symbol_right== True:
            cprint('Symbol found on right', 'red')

sum = 0

for i in range(0, len(data)):
    j = 0
    while j < len(data[i]):
        if data[i][j].isdigit() == True:
            print("Digit: " + str(data[i][j]))
            number = getnumber(i, j)
            print(f"i: {i}   j: {j}")
            
            print(checksymbol(i, j, number))
        #     if checksymbol(i,j, number):
        #         sum += number
        #     j += len(str(number))-1
        j += 1

print(sum)