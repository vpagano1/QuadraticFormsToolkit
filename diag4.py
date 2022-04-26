from math import sqrt, ceil
def diag(a,b,c,d,e,f,k):
    v = max(ceil(sqrt(k)),1)
    for xs in range(-v,v+1):
        x = -xs
        for ys in range(-v,v+1):
            y = -ys
            for zs in range(-v,v+1):
                z = -zs
                for ts in range(-v,v+1):
                    t = -ts
                    if a*x**2+b*y**2+c*z**2+d*t**2+2*e*y*t+2*f*z*t==k:
                        return (True, (x,y,z,t))
    return (False, (-1,-1,-1,-1))

def diagonal(a,b,c,d,e,f):
    for k in range(16):
        if not diag(a,b,c,d,e,f,k)[0]:
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
            d = input("d> ")
            e = input("e> ")
            f = input("f> ")
        n = input("n> ")
        try:
            a = int(a)
            b = int(b)
            c = int(c)
            d = int(d)
            e = int(e)
            f = int(f)
            if n=="universal" or n=="u" or n=="uni":
                if diagonal(a,b,c,d,e,f): print("Universal")
                n = 0
                hide = True
            else: n = int(n)
            done = True
        except Exception:
            done = False
            print("Oops! Only integers please!")
    same = True
    rep = diag(a,b,c,d,e,f,n)
    if not hide:
        if rep[0]: print("Represented:",rep[1])
        if not rep[0]: print("Not represented")
    # again = input("Again? (y/n)")
    # print("")
    # if again==n: loop = False
