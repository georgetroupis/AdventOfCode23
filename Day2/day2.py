def day2():
    file = open('Day2/input.txt', 'r')
    lines = file.readlines()

    idSum = 0

    RED_TOTAL = 12
    GREEN_TOTAL = 13
    BLUE_TOTAL = 14

    for line in lines:

        gameId = int(line.split(" ")[1][:-1])

        impossibleGame = False

        colonIndex = line.find(":")

        for subGame in line.rstrip()[colonIndex + 1:].split(";"):

            print("subGame", subGame)

            for numColour in subGame.split(','):

                numColour = numColour[1:]

                num, colour = int(numColour.split(" ")[0]), numColour.split(" ")[1]
                if colour == "red" and num > RED_TOTAL:
                    impossibleGame = True

                elif colour == "blue" and num > BLUE_TOTAL:
                    impossibleGame = True
                elif colour == "green" and num > GREEN_TOTAL:
                    impossibleGame = True

                if impossibleGame is True:
                    print('impossible', gameId)
                    break;
            if impossibleGame is True:
                break;

        if not impossibleGame:
            print("possible", gameId)
            idSum += gameId

    print('idSum', idSum)


def day2ext():
    file = open('Day2/input.txt', 'r')
    lines = file.readlines()

    idSum = 0

    for line in lines:

        gameId = int(line.split(" ")[1][:-1])

        colonIndex = line.find(":")

        red = 0
        blue = 0
        green = 0

        for subGame in line.rstrip()[colonIndex + 1:].split(";"):

            print("subGame", subGame)

            for numColour in subGame.split(','):

                numColour = numColour[1:]

                num, colour = int(numColour.split(" ")[0]), numColour.split(" ")[1]
                if colour == "red":
                    red = max(red, num)

                elif colour == "blue":
                    blue = max(blue, num)
                elif colour == "green":
                    green = max(green, num)

        idSum = idSum + (red * green * blue)

    print('idSum', idSum)
