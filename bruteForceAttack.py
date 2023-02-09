from utils import reverseMapping, getHashedString
from decrypt import decrypt
import pdb

def seperateHashAndCipherText(cipherTextWithHash):
    return cipherTextWithHash[:len(cipherTextWithHash)-64], cipherTextWithHash[len(cipherTextWithHash)-64:]


def testBruteForcedKey(cipherTextList, generatedKey):
    for cipherTextWithHash in cipherTextList:
        cipherText, appendedHash = seperateHashAndCipherText(cipherTextWithHash)
        decryptedPlainText = decrypt(cipherText, generatedKey)
        if appendedHash != getHashedString(decryptedPlainText):
            return False
    return True


def bruteForceKeyLength1(cipherTextList):
    for i in range(0, 26):
        generatedKey = reverseMapping[i]
        if (testBruteForcedKey(cipherTextList, generatedKey)):
            return True, generatedKey
    print("Key Length not equal to 1")
    return False, None


def bruteForceKeyLength2(cipherTextList):
    for i in range(0, 26):
        for j in range(0, 26):
            generatedKey = reverseMapping[i] + reverseMapping[j]
            if (testBruteForcedKey(cipherTextList, generatedKey)):
                return True, generatedKey
    print("Key Length not equal to 2")
    return False, None


def bruteForceKeyLength3(cipherTextList):
    for i in range(0, 26):
        for j in range(0, 26):
            for k in range(0, 26):
                generatedKey = reverseMapping[i] + \
                    reverseMapping[j] + reverseMapping[k]
                if (testBruteForcedKey(cipherTextList, generatedKey)):
                    return True, generatedKey
    print("Key Length not equal to 3")
    return False, None


def bruteForceKeyLength4(cipherTextList):
    for i in range(0, 26):
        for j in range(0, 26):
            for k in range(0, 26):
                for l in range(0, 26):
                    generatedKey = reverseMapping[i] + reverseMapping[j] + reverseMapping[k] + reverseMapping[l]
                    if (testBruteForcedKey(cipherTextList, generatedKey)):
                        return True, generatedKey
    print("Key Length not equal to 4")
    return False, None


def bruteForceKey(cipherTextList, maxKeyLength):
    cntKeyLength = 1
    while (cntKeyLength <= maxKeyLength):
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
