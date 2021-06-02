import numpy as np
n=100
success_with_changing=0
success_without_changing=0
for _ in range(n):
    Rand=np.random.randint(1,4)
    a={1:"G",2:"G",3:"G"}
    for i in a.keys():
        if i==Rand:
            a[i]="M"
    #a is a list of doors
    choice=np.random.randint(1,4)
    b=a.copy()
    for i in a.keys():
        if (a[i]!="M" and i!=choice):
            b.pop(i)
            break
    if choice==Rand:
        success_without_changing+=1
    c=b.copy()
    for i in b.keys():
        if(i!=choice):
            c.pop(i)
            break
    if [i for i in c.values()][0]=='M':
        success_with_changing+=1
print(success_with_changing,success_without_changing)