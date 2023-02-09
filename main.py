from encrypt import encrypt
from decrypt import decrypt
from utils import getHashedString, seperateHashAndCipherText
from bruteForceAttack import bruteForceKey


def main():
    plainTextList = ["keshav", "tanmayrajore", "helloworldthisiskeshav",
                     "hellothisiskeshavandwearetestingbruteforcingakey", "thisisthefinalteststringwhichisgreaterthanthepreviousone"]
    key = "lopr"

    cipherTextWithHashes = []
    for plainText in plainTextList:
        hashValue = getHashedString(plainText)
        cipherText = encrypt(plainText, key)
        cipherTextWithHashes.append(cipherText+hashValue)

    for plainText, cipherText in zip(plainTextList, cipherTextWithHashes):
        print(plainText+":    "+cipherText)

    decryptedPlainText = []
    for text in cipherTextWithHashes:
        cipherText, hashValue = seperateHashAndCipherText(text)
        decryptedPlainText.append(decrypt(cipherText, key))

    print()
    print()

    for plainText, decryptedPlainText in zip(plainTextList, decryptedPlainText):
        print(plainText+" : "+decryptedPlainText +
              " : "+str(plainText == decryptedPlainText))

    print()
    print()

    print(bruteForceKey(cipherTextWithHashes, 4))


main()
