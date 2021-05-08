from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os
import sys
key=os.urandom(16)
aesCipher=Cipher(algorithms.AES(key),modes.ECB(),backend=default_backend())
aesEncryptor=aesCipher.encryptor()
ifile,ofile= sys.argv[1:3]
with open(ifile ,'rb') as reader:
    with open(ofile,'wb+') as writer:
        pre_image= reader.read()
        header , body = pre_image[:54], pre_image[54:]
        body+= b'\x00'*(16-(len(body)%16))
        writer.write(header + aesEncryptor.update(body))
        