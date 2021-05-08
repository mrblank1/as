#encryption with CTR method
from cryptography.hazmat.primitives.ciphers import algorithms,modes, Cipher
from cryptography.hazmat.backends import default_backend
import os
class Encrypt_manager(object):
    def __init__(self):
        key=os.urandom(32)
        nonce=os.urandom(16)
        aesContext=Cipher(algorithms.AES(key),modes.CTR(nonce),backend=default_backend())
        self.encryptor=aesContext.encryptor()
        self.decryptor=aesContext.decryptor()
    def update_encryptor(self,message):
        return self.encryptor.update(message)
    def finalize_encryptor(self):
        return self.encryptor.finalize()
    def update_decryptor(self,ciphertext):
        return self.decryptor.update(ciphertext)
    def finalize_decryptor(self):
        return self.decryptor.finalize()
message=[
    b'fuck fuck fuck ',
    b'Medium fuck Medium fuck',
    b'Large fuck Large fuck Large fuck'
]
manager=Encrypt_manager()
ciphertext=[]
for m in message:
    ciphertext.append(manager.update_encryptor(m))
ciphertext.append(manager.finalize_encryptor())
for c in ciphertext:
    print('recovered',manager.update_decryptor(c))
print('recovered',manager.finalize_decryptor())