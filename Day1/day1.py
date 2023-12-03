def day1():
    file = open('Day1/input.txt', 'r')
    lines = file.readlines()

    count = 0

    for line in lines:
        filteredLine = ''.join(char for char in line if not char.isalpha()).rstrip()
        newNum = int(''.join(filteredLine[0] + filteredLine[-1]))
        count += newNum
    print('count', count)


def day1ext():
    file = open('Day1/input.txt', 'r')
    lines = file.readlines()

    newDict = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }

    count = 0
    for line in lines:

        line = line.rstrip()
        filteredLine = ''.join(char for char in line if not char.isalpha()).rstrip()

        lowestIndex = 10000
        lowValue = 'ten'

        highestIndex = -1
        highValue = 'ten'
        for key in newDict.keys():
            ind = line.find(key)
            rind = line.rfind(key)
            lowestIndex = min(ind, lowestIndex) if ind > -1 else lowestIndex
            highestIndex = max(rind, highestIndex) if rind > -1 else highestIndex
            # if line.rstrip() == "vggvnhqkjseventwo4onetwonftrnd":
            #     print("key", key)
            #     print("highestIndex", highestIndex)
            #     print("ind", ind)
            if ind == lowestIndex:
                lowValue = newDict[key]

            if rind == highestIndex:
                highValue = newDict[key]

        # print("highValue", highValue)
        # print("lowValue", lowValue)
        first = filteredLine[0]
        if lowestIndex < line.find(first):
            first = lowValue

        last = filteredLine[-1]
        # print(last)
        # print('highestIndex', highestIndex)
        if highestIndex > line.rfind(last):
            last = highValue

        # print(line)
        # print(first, last)
        # print('\n')
        newNum = int(''.join([str(first), str(last)]))
        count += newNum
    print('count', count)