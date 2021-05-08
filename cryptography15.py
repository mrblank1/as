#encrypting image by the use of CBC
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms,modes
import os
import sys
class Encrypt_manger(object):
    def __init__(self):
        key=os.urandom(32)
        iv=os.urandom(16)
        aesContext=Cipher(algorithms.AES(key),modes.CBC(iv),backend=default_backend())
        self.encrypt= aesContext.encryptor()
        self.decrypt= aesContext.decryptor()
        self.padder=padding.PKCS7(128).padder()
        self.unpadder=padding.PKCS7(128).unpadder()

    def update_encrypt(self,message):
        return self.encrypt.update(self.padder.update(message))
    def finalize_encrypt(self):
        return self.encrypt.update(self.padder.finalize())+self.encrypt.finalize()
    def update_decrypt(self,ciphertext):
        return self.unpadder.update(self.decrypt.update(ciphertext))
    def finalize_decrypt(self):
        return self.unpadder.update(self.decrypt.finalize())+self.unpadder.finalize()
ifile,ofile,decrypt_file= sys.argv[1:4]
manager=Encrypt_manger()
with open (ifile , 'rb') as reader:
    with open (ofile,'wb+') as writer:
        image= reader.read()
        header , body=image[:54], image[54:]
        body+= b'\x00'*(16-(len(body)%16))
        writer.write(header+manager.update_encrypt(body)+manager.finalize_encrypt())
with open(ofile,'rb') as reader:
    with open(decrypt_file, 'wb+') as writer:
        image=reader.read()
        header , body = image[:54] , image[54:]
        writer.write(header+manager.update_decrypt(body)+manager.finalize_decrypt())