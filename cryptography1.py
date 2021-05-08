import string

def create_shift_substitutions(n):
    encoding = {}
    decoding = {}
    alphabet_size = len(string.ascii_uppercase)
    for i in range(alphabet_size):
        letter       = string.ascii_uppercase[i]
        subst_letter = string.ascii_uppercase[(i+n)%alphabet_size]
        encoding[letter]       = subst_letter
        decoding[subst_letter] = letter
    return encoding, decoding
def encode(message,subst):
    cipher=''
    for letter in message:
        if letter in subst:
            cipher +=subst[letter]
        else:
            cipher += letter
    return cipher
def decode(message,subst):
    return encode(message,subst)
def encode1(message,subst):
    return "".join(subst.get(x,x) for x in message)
message='i fucked your mother in a 3 different way and you can\'t do shit about it'.upper()
subst,a= create_shift_substitutions(3)
subst_encode=encode(message.upper(),subst)
print(encode1(message,subst))