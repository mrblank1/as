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
subst,_ = create_shift_substitutions(3)
def printable_substitution(subst):
    mapping= sorted(subst.items())
    alphabetic_line="".join(letter for letter , _ in mapping)
    cipher_line="".join(letter2 for _ , letter2 in mapping)
    return ("{} \n{} ".format(alphabetic_line,cipher_line))
print(printable_substitution(subst))
