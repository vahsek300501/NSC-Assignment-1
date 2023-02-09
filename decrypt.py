from utils import forwardMapping, reverseMapping, constructSquare


def constructSameLengthKey(cipherText, p_key):
    q = int(len(cipherText)/len(p_key))
    r = int(len(cipherText) % len(p_key))
    key = p_key*q
    key += p_key[:r]
    return key


def decrypt(cipherText, p_key):
    key = constructSameLengthKey(cipherText, p_key)
    table = constructSquare()
    plainText = ""
    for keyChar,char in zip(key,cipherText):
        plainText += reverseMapping[table[forwardMapping[keyChar]].index(char)]
    return plainText