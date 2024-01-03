import re

with open("d2pz1.txt") as file:
    data = file.readlines()

# text = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

powersum = 0

for text in data:
        

    game_number, game_values = text.split(':')
    idRegex = re.compile(r"\d+")
    game_ids = idRegex.findall(game_number)


    valueRegex = re.compile(r"\w+")

    possible = True

    max_red = 0
    max_blue = 0
    max_green = 0
    for game_result in game_values.split(';'):
        for values in game_result.split(','):
            v = valueRegex.findall(values)
            v[0] = int(v[0])
            print(v)
            if v[1] == "red" and v[0] > max_red:
                max_red = v[0]
            if v[1] == "green" and v[0] > max_green:
                max_green = v[0]
            if v[1] == "blue" and v[0] > max_blue:
                max_blue = v[0]
            print("R: " + str(max_red) + ", G: " + str(max_green) + ", B: " + str(max_blue))
        print('************')
    power = max_red*max_blue*max_green
    print(power)
    powersum += power
    print('______________________')
print(powersum)