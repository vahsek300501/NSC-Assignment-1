import hashlib
from encrypt import encrypt
from decrypt import decrypt

def getHashedString(text):
    return hashlib.sha256(text.encode()).hexdigest()

def main():
    text = "hellothisiskeshav"
    key = "abcd"
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

main()