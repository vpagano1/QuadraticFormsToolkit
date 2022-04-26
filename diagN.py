from math import sqrt, ceil

def evalQuad(coeff,entries):
    rank = len(coeff)
    if rank != len(entries):
        raise Exception("Length of coefficients must match length of entries.")
    n = 0
    for i in range(rank):
        n += coeff[i]*entries[i]**2
    return n

def makeZeros(n):
    zeros = []
    for i in range(n):
        zeros.append(0)
    return zeros

def clock(watch,m):
    watch[0] = (watch[0]+1)%(m+1)
    for i in range(len(watch)):
        if watch[i] == 0 and i<len(watch)-1:
            watch[i+1] = (watch[i+1]+1)%(m+1)
        elif watch[i] == 0 and i==len(watch)-1:
            watch = True
        else:
            break
    return watch

def represents(coeff,k):
    v = max(ceil(sqrt(k)),1)
    rank = len(coeff)
    entries = makeZeros(rank)
    while entries != True:
        if evalQuad(coeff, entries) == k:
            return (True, entries)
        entries = clock(entries,v)
    return (False, -1)

def universal(coeff):
    for k in range(16):
        if not represents(coeff,k)[0]:
            print(k,"fails")
            return False
    return True

def get_coeffs():
    empty = False
    coeff = []
    while not empty:
        new_coeff = input("#> ")
        empty = new_coeff==""
        if not empty:
            try:
                int_coeff = int(new_coeff)
                coeff.append(int_coeff)
            except ValueError:
                print("Integers only, please!")
    return coeff

restart = True
while True:
    if restart:
        qform = get_coeffs()
        restart = False
    n = input("> ")
    if n == "":
        pass
    elif n in ["p", "print"]:
        print(qform)
    elif n in ["universal", "u", "uni"]:
        if universal(qform): print("Universal!")
    elif n in ["quit","q","exit","done"]:
        restart = True
    elif n in ["list", "l", "until", "unt"]:
        notinteger = True
        while notinteger:
            try:
                notinteger = False
                k = int(input(">> "))
                for i in range(k+1):
                    rep = represents(qform, i)
                    if rep[0]:
                        print(i,"represented!",rep[1])
                    elif not rep[0]:
                        print(i,"not represented!")
            except ValueError:
                notinteger = True
                print("Integers only, please!")
    else:
        try:
            nint = int(n)
            rep = represents(qform, nint)
            if rep[0]:
                print("Represented!",rep[1])
            elif not rep[0]:
                print("Not represented!")
        except ValueError:
            print("Integers only, please!")
