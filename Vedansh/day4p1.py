with open('d4pz1.txt') as file:
    data = file.readlines()

ans = 0

for line in data:
    first, rest = line.split("|")
    the_id, card = first.split(":")
    card_nums = [int(x) for x in card.split()]
    rest_nums = [int(x) for x in rest.split()]
    val = len(set(card_nums) & set(rest_nums))
    print(val)
    if val > 0:
        ans += 2**(val-1)
print(ans)