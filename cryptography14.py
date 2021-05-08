#cryptography with the pair key and iv and symetrical and it doesn't reuse the key and iv
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms , modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os
class Encrypt_manger(object):
    def __init__(self):
        key=os.urandom(32)
        iv=os.urandom(16)
        aesContex=Cipher(algorithms.AES(key),modes.CBC(iv),backend=default_backend())
        self.encryptor=aesContex.encryptor()
        self.decryptor=aesContex.decryptor()
        self.padder=padding.PKCS7(128).padder()
        self.unpadder= padding.PKCS7(128).unpadder()
    def update_encryptor(self,message):
        return  self.encryptor.update(self.padder.update(message))
    def finalize_encryptor(self):
        return self.encryptor.update(self.padder.finalize())+self.encryptor.finalize()
    def update_decryptor(self,message):
        return self.unpadder.update(self.decryptor.update(message))
    def finalize_decryptor(self):
        return self.unpadder.update(self.decryptor.finalize())+self.unpadder.finalize()
manager=Encrypt_manger()
plaintext=[
    b'fuck fuck fuck',
    b'Mfuck Mfuck Mfuck Mfuck Mfuck',
    b'Lfuck Lfuck Lfuck Lfuck Lfuck Lfuck Lfuck'
]
ciphertext=[
]
for m in plaintext:
    ciphertext.append(manager.update_encryptor(m))
ciphertext.append(manager.finalize_encryptor())
for c in ciphertext:
    print('recovered',manager.update_decryptor(c))
print(manager.finalize_decryptor())