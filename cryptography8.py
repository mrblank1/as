from numpy.random import randint
import hashlib
import string
from time import time
def timer(func):
    def wrapper(*args):
        a=time()
        func(*args)
        print('function took:{}'.format(time()-a))
    return wrapper

initial_letter=bytes(string.ascii_lowercase[randint(26)],'utf-8')
hashed=hashlib.md5(initial_letter).hexdigest()
@timer
def checker(a):
    v=''
    for i in string.ascii_lowercase:
        v=hashlib.md5(bytes(i,'utf-8')).hexdigest()
        print(v,'\n',i)
        if(a==v):
            break
checker(hashed)