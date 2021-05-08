import os
import operator
a=os.urandom(16)
print(a)
b=b'\x02'*16
c=[]
for i,j in enumerate(a,0):
    c.append(operator.xor(b[i],j))
print(c)
a=c.copy()
c=b''
for i,j in enumerate(a,0):
    c+=operator.xor(b[i],j).to_bytes(1,'little')
print(c)
