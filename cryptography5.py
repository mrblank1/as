from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.backends import default_backend
import os
salt=os.urandom(16)
kdf=Scrypt(salt=salt,length=32 ,n=2**14,r=8,p=1,backend=default_backend())
key=kdf.derive(b'motherfucking password')
print(key,'\n',salt)    