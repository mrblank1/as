#the cryptogrophy with cbc method and use the same key and iv for all but symetrical
from cryptography.hazmat.primitives.ciphers import Cipher, modes,algorithms
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os 
class Encryptor_manager(object):
    def __init__(self):
        self.key=os.urandom(32)
        self.iv=os.urandom(16)
    def encryptor(self,message):
        encryptor=Cipher(algorithms.AES(self.key),modes.CBC(self.iv),backend=default_backend()).encryptor()
        padder=padding.PKCS7(128).padder()
        padded_message= padder.update(message)
        padded_message+=padder.finalize()
        ciphertext=encryptor.update(padded_message)
        ciphertext+=encryptor.finalize()
        return ciphertext
    def decryptor(self,ciphertext):
        decryptor=Cipher(algorithms.AES(self.key), modes.CBC(self.iv), backend=default_backend()).decryptor()
        unpadder= padding.PKCS7(128).unpadder()
        message=decryptor.update(ciphertext)
        message+= decryptor.finalize()
        unpadded_message=unpadder.update(message)
        unpadded_message+= unpadder.finalize()
        return unpadded_message
plaintext=[
    b'fuck fuck fuck',
    b'mfuck mfuck mfuck mfuck',
    b'Lfuck Lfuck Lfuck Lfuck Lfuck Lfuck'
]
ciphertext=[]
encryptor=Encryptor_manager()
for m in plaintext:
    ciphertext.append(encryptor.encryptor(m))
for c in ciphertext:
    print('recovered',(encryptor.decryptor(c)))

