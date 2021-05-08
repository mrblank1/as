from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.backends import default_backend
import os
key=b'\x95\xda\nr\x0b\xed\xe8:4Q\xb7\x9f\xf8\xe0\x953\xadBvUN\x17KC\xbd\xdb\x93?:\x91O\x9f'
salt=b'\x1dkC;\xda\x11^\xa4zMb\xcfr`\r\x1b'
kdf=Scrypt(salt=salt,length=32 ,r=8,p=1,n=2**14,backend=default_backend())
kdf.verify(b'motherfucking password',key)
print("Success! (Exception if mismatch)")