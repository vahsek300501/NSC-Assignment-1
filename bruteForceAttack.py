def bruteForceKeyLength1(cipherTextList):
    pass


def bruteForceKeyLength2(cipherTextList):
    pass


def bruteForceKeyLength3(cipherTextList):
    pass


def bruteForceKeyLength4(cipherTextList):
    pass


def bruteForceKey(cipherTextList, maxKeyLength):
    cntKeyLength = 1
    while (cntKeyLength < maxKeyLength):
        if cntKeyLength == 1:
            isKeyFound, key = bruteForceKeyLength1(cipherTextList)
            if isKeyFound:
                return True, key

        elif cntKeyLength == 2:
            isKeyFound, key = bruteForceKeyLength2(cipherTextList)
            if isKeyFound:
                return True, key

        elif cntKeyLength == 3:
            isKeyFound, key = bruteForceKeyLength3(cipherTextList)
            if isKeyFound:
                return True, key

        elif cntKeyLength == 4:
            isKeyFound, key = bruteForceKeyLength4(cipherTextList)
            if isKeyFound:
                return True, key
        
        else:
            break        
        cntKeyLength += 1
    return False, None
