
from termcolor import cprint

with open("/Users/pk/proj/adventOfCode/Puneet/d3_final_input.txt") as file:
    data = file.readlines()

# with open('/Users/pk/proj/adventOfCode/Puneet/d3_sample_input.txt') as file:
#     data = file.readlines()

def getnumber(row, col):
    number = 0
    while data[row][col].isdigit() == True:
        number = number*10 + int(data[row][col])
        col += 1
    return number

def containsSymbol(row, start_col, end_col):
    # print(data[row])
    for col in range(start_col, end_col):
        # print('checking symbol at row: ' + str(row) + ' col : ' + str(col) + ' for symbol : ' + data[row][col])
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
        
        #check to the top
        top_row = max(row-1,0)
        start_col = max(col-1,0)
        end_col = min(col+len(str(number))+1, len(data[row]))
        symbol_top = containsSymbol(top_row, start_col, end_col)
        if symbol_top == True:
            cprint('Symbol found on top', 'blue')  

        # check to the bottom
        bottom_row = min(row+1, len(data)-1)
        start_col = max(col-1,0)
        end_col = min(col+len(str(number))+1, len(data[row]))
        symbol_bottom = containsSymbol(bottom_row, start_col, end_col)
        if symbol_bottom == True:
            cprint('Symbol found on bottom', 'yellow')
        cprint('Symbol left : ' + str(symbol_left) + ' Symbol right : ' + str(symbol_right) + ' Symbol top : ' + str(symbol_top) + ' Symbol bottom : ' + str(symbol_bottom), 'green')
        return symbol_left or symbol_right or symbol_top or symbol_bottom

sum = 0

for row in range(0, len(data)):
    col = 0
    while col < len(data[row]):
        if data[row][col].isdigit() == True:
            cprint("Digit: " + str(data[row][col]), "light_yellow")
            number = getnumber(row, col)
            print(f"Row: {row}   Col: {col}   Number: {number}")
            # print(checksymbol(row, col, number))
            if checksymbol(row, col, number):
                sum += number
                cprint("Adding: " + str(number) + "  Sum: " + str(sum), "light_red")
            else:
                cprint("Not adding: " + str(number) + "  Sum: " + str(sum), "light_green")
            col += len(str(number))-1
        col += 1

cprint("Sum of the numbers : " + str(sum), "light_red")