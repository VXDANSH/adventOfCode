from termcolor import colored, cprint

def containsSymbol(row, start_col, end_col):
    #check if symbol is around
    cprint('start col : ' + str(start_col) + ' end col : ' + str(end_col), "cyan")
    for col in range(start_col, end_col):
        print('checking symbol at row ' + str(row) + ' col : ' + str(col) + 'for symbol : ' + str(data[row][col]))
        if data[row][col].isdigit() == False and data[row][col] != '.':
            return True
    return False

def checkSymbol(row,col, number):
    symbol = False
    #check left
    print ('I : ' + str(row) + ' J : ' + str(col))
    symbol_left = containsSymbol(row, max(col-1, 0), col)
    if symbol_left == True:
        cprint("symbol found on left", "green")
    #check right
    length = len(data[row])
    print('length of row: ' + str(length))
    print('col + len(str(number)) + 1 : ' + str(col+len(str(number))))
    cprint('row checking right ' + str(row), "light_red")
    symbol_right = containsSymbol(row, min(col+len(str(number)), len(data[row])), min(col+len(str(number))+1, len(data[row])))
    if symbol_right == True:
        cprint("symbol found on right", "red")
    #check row above 
    left_col=max(col-1, 0)
    right_col=min(col+len(str(number))+1, len(data[row]))
    top_row=max(row-1, 0)
    symbol_top = containsSymbol(top_row, left_col, right_col)
    print('left col : ' + str(left_col) + ' right col : ' + str(right_col) + ' top row : ' + str(top_row))
    if symbol_top == True:
        cprint("symbol found on top", 'light_blue')
    #check row below
    bottom_row=min(row+1, len(data)-1)
    left_col=max(col-1, 0)
    right_col=min(col+len(str(number))+1, len(data[row]))
    symbol_bottom = containsSymbol(bottom_row, left_col, right_col)
    print('left col bottom : ' + str(left_col) + ' right col bottom: ' + str(right_col) + ' bottom row : ' + str(bottom_row))
    if symbol_bottom == True:
        cprint("symbol found on bottom", 'yellow')
    return True

def getNumber(i,j):
    n=0
    if data[i][j-1].isdigit() == True:
        return None
    while data[i][j].isdigit() == True:
        n = n*10 + int(data[i][j])
        j += 1
    return n
          

## MAIN PROGRAM          

with open("/Users/pk/proj/adventofcode/day 3/d3input.txt") as file:
    data = file.readlines()

for i in range(0, len(data)):
    data[i] = data[i].strip('\n')

print(data)

sum = 0

for row in range(0, len(data)):
    col = 0
    while col < len(data[row]):
        # print("Jfor : " + str(j))
        if data[row][col].isdigit() == True:
            print("Digit : " + str(data[row][col]))
            number = getNumber(row, col)
            print("Number : " + str(number))
            # print("Jloop : " + str(j))
            symbol = checkSymbol(row, col, number)
            col+= len(str(number))-1
            #check if symbol 
        col+=1

    print("**********")
        
        
        





