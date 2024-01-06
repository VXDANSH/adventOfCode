with open('d4pz1.txt') as file:
    data = file.readlines()

ans = 0

for line in data:
    first, rest = line.split("|")
    the_id, card = first.split(":")
    card_nums = [int(x) for x in card.split()]
    rest_nums = [int(x) for x in rest.split()]
    val = len(set(card_nums) & set(rest_nums))
    copies = []
    for i in range(0, val-1):
        character = ''
        while character != ' ':
            character = the_id[-i - 1]
print(copies)