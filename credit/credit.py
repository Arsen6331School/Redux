def getCCN():
    while True:
        try:
            height = int(input("Credit Card Number: "))
        except ValueError:
            continue
        return height


def toIntList(n):
    return [int(d) for d in str(n)]


def isValid(ccn):
    intList = toIntList(ccn)
    oddList = intList[-1::-2]
    evenList = intList[-2::-2]
    checksum = 0
    for even in evenList:
        checksum += sum(toIntList(even * 2))
    checksum += sum(oddList)
    return checksum % 10 == 0


ccn = getCCN()

if not isValid(ccn):
    print("INVALID")
    exit()

ccnStr = str(ccn)
firstTwo = int(ccnStr[:2])

if firstTwo >= 40 and firstTwo <= 49:
    print("VISA")
elif firstTwo in [34, 37]:
    print("AMEX")
elif firstTwo >= 50 and firstTwo <= 55:
    print("MASTERCARD")
else:
    print("INVALID")
