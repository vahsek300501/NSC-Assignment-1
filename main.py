from encrypt import encrypt
from decrypt import decrypt
from utils import getHashedString
from bruteForceAttack import bruteForceKey

def main():
    text = "hellothisiskeshavandwearetestingbruteforcingakey"
    key = "al"
    print("Plain text is: "+text)
    cipherText = encrypt(text,key)
    cipherText += getHashedString(text)
    print("Cipher text is: "+cipherText)
    
    hashValue = cipherText[len(cipherText)-64:]
    encryptedCipherText = cipherText[:len(cipherText)-64]
    decryptedCipherText = decrypt(encryptedCipherText,key)
    print("Decrypted cipher text: "+decryptedCipherText)
    print("Hashed value: "+getHashedString(decryptedCipherText))
    print("Obtained hash value: "+hashValue)
    print(getHashedString(decryptedCipherText) == hashValue)
    print()
    print()
    print()
    print()
    print(bruteForceKey([cipherText],4))
main()