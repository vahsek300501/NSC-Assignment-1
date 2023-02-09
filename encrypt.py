from utils import forwardMapping, constructSquare
import pdb

def constructSameLengthKey(plainText,p_key):
	q = int(len(plainText)/len(p_key))
	r = int(len(plainText)%len(p_key))
	key = p_key*q
	key += p_key[:r]
	return key

def encrypt(plainText,p_key):
	encryptionKey = constructSameLengthKey(plainText,p_key)
	table = constructSquare()
	cipherText = ""
	for char,keyChar in zip(plainText,encryptionKey):
		cipherText += table[forwardMapping[keyChar]][forwardMapping[char]]
	return cipherText


