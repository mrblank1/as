import hashlib
a=""
with open("first_logfile.txt","rb") as f:
    a=f.read()
    md5hash=hashlib.md5(a).hexdigest()
    f.close()
print(md5hash)