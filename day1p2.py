# sample = ['1abc2', 'pqr3fdskj8as', 'afd1asdf2dfd6asdf7asdf5sd', 'treb7uchet']

sample = []

with open("/Users/vedansh/Desktop/AdventOfCode/pz2sample.txt") as w:
    sample = w.readlines()

dgwords = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

sum = 0

for s in sample:
    foundgs = []

    for dgword in dgwords:
        # if s.find(dgword) != -1:
        #     mydict = {}
        #     mydict['index'] = s.find(dgword)
        #     mydict['word'] = dgword
        #     foundgs.append(mydict)
        index = 0
        while index < len(s):
            index = s.find(dgword, index)
            if index == -1:
                break
            word = {}
            word['index'] = index
            word['word'] = dgword
            foundgs.append(word)
            index += len(dgword)

    mindict = {}
    maxdict = {}

    if foundgs:
        mindict = min(foundgs, key=lambda x:x['index'])
        maxdict = max(foundgs, key=lambda x:x['index'])
    print(s)
    print(mindict)
    print(maxdict)      
    right_digit = None
    rightdigind = None
    for j in s[::-1]:
        if j.isdigit() == True:
            right_digit = int(j)
            rightdigind = len(s)-(s[::-1].index(j))-1
            break

    left_digit = None
    leftdigind = None
    for j in s:
        if j.isdigit() == True:
            left_digit = int(j)
            leftdigind = s.index(j)
            break
    print(left_digit)
    print(leftdigind)
    print("right digit : " + str(right_digit))
    print("right digit index : " + str(rightdigind))
    if left_digit != None and foundgs:
        if mindict['index'] < leftdigind:
            sum += dgwords.index(mindict['word'])*10
        else:
            sum += left_digit*10
    elif not foundgs:
        sum += left_digit*10
    elif left_digit == None:
        sum += dgwords.index(mindict['word'])*10

    #-----------------------------------------------------------------------------------------------------

    if right_digit != None and foundgs:
        
        if maxdict['index'] > rightdigind:
            sum += dgwords.index(maxdict['word'])
        else:
            sum += right_digit
    elif not foundgs:
        sum += right_digit
    elif right_digit == None:
        sum += dgwords.index(maxdict['word'])

    print(sum)