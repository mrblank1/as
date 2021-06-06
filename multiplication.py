from numpy import random 
import time
Number=input("How many rounds do you want?\n")
Difficulty=input("the difficluty lvl (1..5)\n")
def number_generator(a):
    if a==1:
        return random.randint(10,100),random.randint(10,100)
    if a==2:
        return random.randint(100,200),random.randint(10,100)
    if a==3:
        return random.randint(100,200),random.randint(100,200)
    if a==4:
        return random.randint(100,500),random.randint(100,500)
    if a==5:
        return random.randint(500,1000),random.randint(500,1000)
def check(n1,n2):
    if n1==n2:
        print("Correct!")
    else :
        print(f"Fuck your mama the answer was {n2}")
for i in range(int(Number)):
    n1,n2=number_generator(int(Difficulty))
    print(f"{n1} * {n2} =? ",end="\n")
    start_time=time.time()
    entry=input("answer=? ")
    check(int(entry),n1*n2)
    end_time=time.time()
    print(f"{end_time-start_time:.2f} seconds")
