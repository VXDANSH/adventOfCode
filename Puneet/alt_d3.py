grid = open('/Users/pk/proj/adventOfCode/Puneet/d3_sample_input.txt').read().splitlines()
# grid = open('/Users/pk/proj/adventOfCode/Puneet/d3_final_input.txt').read().splitlines()

cs = set()

#find the symbols and the starting top left row, col of the digits surrounding the symbol
for r, row in enumerate(grid):
    for c, ch in enumerate(row):
        # print('r : ' + str(r) + ' c : ' + str(c) + ' ch : ' + str(ch))
        if ch.isdigit() or ch == ".":
            continue
        for dr in range(r - 1, r + 2):
            print('dr : ' + str(dr))
            for dc in range(c - 1, c + 2):
                # print('dc : ' + str(dc))
                if dr < 0 or dr >= len(grid) or dc < 0 or dc >= len(grid[dr]) or not grid[dr][dc].isdigit():
                    continue
                while dc > 0 and grid[dr][dc - 1].isdigit():
                    # print('dc : ' + str(dc) + ' grid[dr][dc - 1] : ' + str(grid[dr][dc - 1]) + ' dr : ' + str(dr))
                    dc -= 1
                cs.add((dr, dc))
                # print('cs : ' + str(cs))

ns = []

for r, c in cs:
    s = ""
    while c < len(grid[r]) and grid[r][c].isdigit():
        s += grid[r][c]
        c += 1
    ns.append(int(s))

print(sum(ns))