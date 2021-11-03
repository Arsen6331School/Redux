def getValidHeight():
    while True:
        try:
            height = int(input("Height: "))
        except ValueError:
            continue
        if height >= 1 and height <= 8:
            return height


def printRow(height, rowNum):
    amtSpaces = height - rowNum
    print(" " * amtSpaces, end="")
    print("#" * rowNum, end="")
    print("  ", end="")
    print("#" * rowNum)


def printPyramid(height):
    for i in range(1, height + 1):
        printRow(height, i)


height = getValidHeight()
printPyramid(height)