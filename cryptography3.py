import string
def creat_substitution(n):
    encoding={}
    decoding={}
    alphabet_size=len(string.ascii_uppercase)
    for i in range(alphabet_size):
        letter=string.ascii_uppercase[i]
        subst_letter=string.ascii_uppercase[(i+n)%alphabet_size]
        encoding[letter]=subst_letter
        decoding[subst_letter]=letter
    return encoding, decoding
def decode(message,subst):
    return "".join(subst.get(x,x) for x in message)
n=0
The_message=input("The message is:>> ")
while True:
    _ , decoding= creat_substitution(n)
    print("{}\nis this right?".format(decode(The_message, decoding)))
    response=input("Y/N? ")
    if response=="Y" or response=="y" or response=="yes":
        break
    elif response=="N" or response=="n" or response=="no":
        n+=1
    else:
        raise ValueError("Wrong argument")

