from cryptography.hazmat.primitives.ciphers import algorithms,modes,Cipher
from cryptography.hazmat.backends import default_backend
import os
key=os.urandom(16)
aesCipher=Cipher(algorithms.AES(key),modes.ECB(),backend=default_backend())
aesEncryptor=aesCipher.encryptor()
aesDecryptor=aesCipher.decryptor()
aesEncryptor.update(b'fuck fuck your mother ')
print(aesDecryptor.update(aesEncryptor.update(b'000000000000')))
