def generator(alphabet,max_len):
    if max_len<=0:return
    for c in alphabet:
        yield c
    for c in alphabet:
        for next in generator(alphabet,max_len-1):
            yield c+next
for i in generator('ab',2):
    print(i)