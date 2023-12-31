# -*- coding: utf-8 -*-
"""RSA

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Amv0nXEoMsyG1iyNsdJZu28ZCVt0KtZ6
"""

UID='118406473'
Last_Name='Kanna'
First_Name='Suprajha'

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import binascii

def rsa_enc_public(inputblock, keypair):
  pubKey = keyPair.publickey()
  encryptor = PKCS1_v1_5.new(pubKey)
  CT = encryptor.encrypt(inputblock)
  #print("Encrypted message is:",binascii.hexlify(CT))
  return CT
  #prints the extracted keys from the keypair
  #pubKey = keyPair.publickey()
  #print(f"Public key:  (n={hex(pubKey.n)}, e={hex(pubKey.e)})")
  #pubKeyPEM = pubKey.exportKey()

  #print(f"Private key: (n={hex(pubKey.n)}, d={hex(keyPair.d)})")
  #privKeyPEM = keyPair.exportKey()

def rsa_dec_private(encrypted, keypair):
  # encrypted is the ciphertext in byte sequence
  # Decryption of RSA
  decryptor = PKCS1_v1_5.new(keyPair)
  PT = decryptor.decrypt(encrypted, None)
  #print("Decrypted message is:",PT)
  return PT

if __name__ == "__main__":
    keyPair = RSA.generate(2048) #This line generates the keypair.
    inputblock = b'A message for encryption'
    encrypted = rsa_enc_public(inputblock,keyPair)
    print("Encrypted message is:",binascii.hexlify(encrypted))
    decrypted = rsa_dec_private(encrypted,keyPair)
    print("Decrypted message is:",decrypted)