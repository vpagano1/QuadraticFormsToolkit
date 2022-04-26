from math import sqrt, ceil
def diag(a,b,c,k):
    v = max(ceil(sqrt(k)),1)+1
    for x in range(v):
        for y in range(v):
            for z in range(v):
                # print(x,y,z)
                if a*x**2+b*y**2+c*z**2==k:
                    return (True, (x,y,z))
    return (False, (-1,-1,-1))

def diagonal(a,b,c):
    for k in range(16):
        if not diag(a,b,c,k)[0]:
            print(k,"fails")
            return False
    return True

loop = True
same = False
while loop:
    done = False
    hide = False
    while not done:
        if not same:
            a = input("a> ")
            b = input("b> ")
            c = input("c> ")
        n = input("n> ")
        try:
            a = int(a)
            b = int(b)
            c = int(c)
            if n=="universal" or n=="u" or n=="uni":
                if diagonal(a,b,c): print("Universal!")
                n = 0
                hide = True
            else: n = int(n)
            done = True
        except Exception:
            done = False
            print("Oops! Only integers please!")
    same = True
    rep = diag(a,b,c,n)
    if not hide:
        if rep[0]: print("Represented",rep[1])
        if not rep[0]: print("Not represented")
    # again = input("Again? (y/n)")
    # print("")
    # if again==n: loop = False
