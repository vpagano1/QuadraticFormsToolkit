from math import sqrt, ceil
from sys import exit
from sympy import primerange
import numpy as np

def evalQuad(quad,entries):
    rank = len(quad)
    # if rank > 1:
    if rank != len(entries): raise Exception("Number of variables must match length of entries.")
    return np.matmul(entries,np.matmul(quad,np.transpose(entries)))

def make_zeros(n):
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

def represents(quad,k):
    v = max(ceil(sqrt(k)),1)
    rank = len(quad)
    entries = make_zeros(rank)
    while entries != True:
        if evalQuad(quad, entries) == k:
            return (True, entries)
        try: entries = clock(entries,v)
        except IndexError: exit()
    return (False, -1)

def universal(quad):
    for k in range(16):
        if not represents(quad,k)[0]:
            print(k,"fails")
            return False
    return True

def get_quad():
    empty = False
    diag = []
    while not empty:
        new_diag = input("#> ")
        empty = new_diag==""
        if not empty:
            try:
                int_diag = int(new_diag)
                diag.append(int_diag)
            except ValueError:
                print("Integers only, please!")
    quad = []
    for i in range(len(diag)):
        quad.append(make_zeros(len(diag)))
    for i in range(len(diag)): quad[i][i] = diag[i]
    for i in range(len(diag)):
        for j in range(i+1,len(diag)):
            quad[i][j] = "X"
            print_quad(quad)
            new_entry = get_integer("##> ",0) # (r"+str(i+1)+",c"+str(j+1)+")
            quad[i][j] = new_entry
            quad[j][i] = new_entry
    # for i in range(len(diag)):
    #     for j in range(i):
    #         # print(" at r"+str(i)+",c"+str(j)+"; replacing "+str(quad[i][j])+" with "+str(quad[j][i]))
    #         quad[i][j] = quad[j][i]
    print("Quadratic form is:")
    print_quad(quad)
    return quad

def print_quad(quad):
    for i in range(len(quad)):
        print("[", end="")
        for j in range(len(quad)):
            if j != len(quad)-1:
                print(quad[i][j], end=" ")
            else:
                print(quad[i][j], end="]\n")
            

def get_integer(input_string, default=None):
    notinteger = True
    while notinteger:
        try:
            notinteger = False
            stdin = input(input_string)
            if stdin == "" and default != None: k = default
            else: k = int(stdin)
        except ValueError:
            notinteger = True
            print("Integers only, please!")
    return k

def getSquares(p):
    squares = []
    antisquares = []
    for i in range(p):
        squares.append((i**2)%p)
    for i in range(p):
        if not i in squares: antisquares.append(i)
    squares.pop(squares.index(0))
    return (squares, antisquares)

def square2class(k):
    for m in [1,3,5,7]:
        represented_bool = False
        for i in range(k+1):
            rep = represents(quad, 8*i+m)
            if rep[0]:
                print(" u"+str(m)+":",8*i+m,"represented!",rep[1],"(n="+str(i)+": 8*"+str(i)+"+"+str(m)+")")
                represented_bool = True 
                break
        if not represented_bool:
            print(" u"+str(m)+": not represented up to "+str(8*k+m)+", (n="+str(k)+": 8*"+str(k)+"+"+str(m)+")")

        represented_bool = False
        for i in range(k+1):
            rep = represents(quad, 2*(8*i+m))
            if rep[0]:
                print("2u"+str(m)+":",2*(8*i+m),"represented!",rep[1],"(n="+str(i)+": 2*(8*"+str(i)+"+"+str(m)+") )")
                represented_bool = True
                break
        if not represented_bool:
            print("2u"+str(m)+": not represented up to "+str(2*(8*k+m))+", (n="+str(k)+": 2*(8*"+str(k)+"+"+str(m)+") )")

def psquareclass(p,k):
    squares, antisquares = getSquares(p)

    represented_bool = False
    for i in range(k+1):
        if represented_bool == True: break
        for j in squares:
            rep = represents(quad, p*i+j)
            if rep[0]:
                print(" [1]:",p*i+j,"represented!",rep[1],"(n="+str(i)+": "+str(p)+"*"+str(i)+"+"+str(j)+")")
                represented_bool = True
                break
    if not represented_bool:
        print(" [1]: not represented up to "+str(p*k+max(squares))+", n="+str(k)+": "+str(p)+"*"+str(k)+"+"+str(squares)+")")

    represented_bool = False
    for i in range(k+1):
        if represented_bool == True: break
        for j in antisquares:
            rep = represents(quad, p*i+j)
            if rep[0]:
                print(" [u]:",p*i+j,"represented!",rep[1],"(n="+str(i)+": "+str(p)+"*"+str(i)+"+"+str(j)+")")
                represented_bool = True
                break
    if not represented_bool:
        print(" [u]: not represented up to "+str(p*k+max(antisquares))+", n="+str(k)+": "+str(p)+"*"+str(k)+"+"+str(antisquares)+")")

    represented_bool = False
    for i in range(k+1):
        if represented_bool == True: break
        for j in squares:
            rep = represents(quad, p*(p*i+j))
            if rep[0]:
                print(" [p]:",p*(p*i+j),"represented!",rep[1],"(n="+str(i)+": "+str(p)+"*("+str(p)+"*"+str(i)+"+"+str(j)+") )")
                represented_bool = True
                break
    if not represented_bool:
        print(" [p]: not represented up to "+str(p*k+max(squares))+", n="+str(k)+": "+str(p)+"*("+str(p)+"*"+str(k)+"+"+str(squares)+") )")

    represented_bool = False
    for i in range(k+1):
        if represented_bool == True: break
        for j in antisquares:
            rep = represents(quad, p*(p*i+j))
            if rep[0]:
                print("[pu]:",p*(p*i+j),"represented!",rep[1],"(n="+str(i)+": "+str(p)+"*("+str(p)+"*"+str(i)+"+"+str(j)+") )")
                represented_bool = True
                break
    if not represented_bool:
        print("[pu]: not represented up to "+str(p*(p*k+max(antisquares)))+", n="+str(k)+": "+str(p)+"*("+str(p)+"*"+str(k)+"+"+str(antisquares)+") )")

restart = True
while True:
    if restart:
        quad = get_quad()
        restart = False
    n = input("> ")
    if n == "":
        pass
    elif n in ["eval", "e", "ev", "evaluate"]:
        entries = []
        for i in range(len(quad)): entries.append(get_integer(">> "))
        print(evalQuad(quad,entries))
    elif n in ["p", "print"]:
        print_quad(quad)
    elif n in ["universal", "u", "uni"]:
        if universal(quad): print("Universal!")
    elif n in ["quit","q","exit","done"]:
        restart = True
    elif n in ["list", "l", "until", "unt"]:
        k = get_integer(">> ")
        for i in range(k+1):
            rep = represents(quad, i)
            if rep[0]:
                print(i,"represented!",rep[1])
            elif not rep[0]:
                print(i,"not represented!")
    elif n in ["list hide", "hide list", "lh", "hl", "hide until", "until hide", "hunt", "unth"]:
        k = get_integer(">> ",1000)
        try:
            for i in range(k+1):
                rep = represents(quad, i)
                if not rep[0]:
                    print(i,"not represented!")
        except KeyboardInterrupt: pass
    elif n in ["u1","u3","u5","u7"]:
        k = get_integer(">> ",30)
        m = int(n[1])
        for i in range(k+1):
            rep = represents(quad, 8*i+m)
            if rep[0]:
                print(8*i+m,"represented!",rep[1],"(n="+str(i)+": 8*"+str(i)+"+"+str(m)+")")
                break
    elif n in ["2u1","2u3","2u5","2u7"]:
        k = get_integer(">> ",30)
        m = int(n[2])
        for i in range(k+1):
            rep = represents(quad, 2*(8*i+m))
            if rep[0]:
                print(2*(8*i+m),"represented!",rep[1],"(n="+str(i)+": 2*(8*"+str(i)+"+"+str(m)+") )")
                break
    elif n in ["2sq", "2-square classes", "2 square classes"]:
        k = get_integer(">> ",30)
        square2class(k)
    elif n in ["psq","p-square classes","p square classes","oddsq"]:
        p = get_integer(">> ",3)
        k = get_integer(">> ",30)
        psquareclass(p, k)
    elif n in ["sq", "squares", "sqs", "square classes"]:
        k = get_integer(">> ",30)
        if len(quad)>=3:
            det = np.linalg.det(quad)
            print("p=2")
            square2class(k)
            for p in primerange(3,det):
                if det%p == 0:
                    print()
                    print("p="+str(p))
                    psquareclass(p,k)
        if len(quad)==2:
            pmax = get_integer(">> ",30)
            print("p=2")
            square2class(k)
            for p in primerange(3,pmax):
                print()
                print("p="+str(p))
                psquareclass(p,k)
    elif n[len(n)-2:len(n)] == "sq":
        k = get_integer(">> ",30)
        try:
            p = int(n[0:len(n)-2])
            psquareclass(p, k)
        except ValueError: print("Integers only before the 'sq', please!")
    elif n in ["p-ladder","pl","ladder"]:
        #[2, 3, 5, 7] 5-ladder?
        #[2, 4, 6, 9]=2[1,2](+)3[1,3] interesting loc uni p-ladder, not 2-ladder
        #[2,2,2,2] a snake, indeed [2,2,4,8] a snake, and k[universal] a snake
        p = get_integer(">> ",2)
        n = get_integer(">> ",1)
        k = get_integer(">> ",5)
        try:
            for i in range(k+1):
                rep = represents(quad, n*p**i)
                if rep[0]:
                    print(str(n)+"*"+str(p)+"^"+str(i),"=",n*p**i,"represented!",rep[1])
                elif not rep[0]:
                    print(str(n)+"*"+str(p)+"^"+str(i),"=",n*p**i,"not represented!")
        except KeyboardInterrupt: pass
    elif n in ["p-ladder list","pll","ladder list"]:
        #[2, 3, 5, 7] 5-ladder?
        #[2, 4, 6, 9]=2[1,2](+)3[1,3] interesting loc uni p-ladder, not 2-ladder
        #[2,2,2,2] a snake, indeed [2,2,4,8] a snake, and k[universal] a snake
        p = get_integer(">> ",2)
        m = get_integer(">> ",5)
        k = get_integer(">> ",5)
        for n in range(1,m+1):
            try:
                for i in range(k+1):
                    rep = represents(quad, n*p**i)
                    if rep[0]:
                        print(str(n)+"*"+str(p)+"^"+str(i),"=",n*p**i,"represented!",rep[1])
                    elif not rep[0]:
                        print(str(n)+"*"+str(p)+"^"+str(i),"=",n*p**i,"not represented!")
            except KeyboardInterrupt: pass
            if n != m: print()
    elif n in ["city","c","main"]:
        det = 1
        for c in quad: det *= c
        Lambda = 8
        for p in primerange(3,det):
            if det%p == 0: Lambda *= p
        try:
            for p in primerange(3,Lambda*100):
                if (p-1)%Lambda == 0: print(p)
        except KeyboardInterrupt: pass
    elif n in ["cityd","cityn","city det","citydet","cd","main det","maind","maindet"]:
        det = get_integer(">> ")
        Lambda = 8
        for p in primerange(3,det):
            if det%p == 0: Lambda *= p
        try:
            for p in primerange(3,Lambda*100):
                if (p-1)%Lambda == 0: print(p)
        except KeyboardInterrupt: pass
    else:
        try:
            nint = int(n)
            rep = represents(quad, nint)
            if rep[0]:
                print("Represented!", rep[1])
            elif not rep[0]:
                print("Not represented!")
        except ValueError:
            print("Integers only, please!")
        except KeyboardInterrupt: pass
