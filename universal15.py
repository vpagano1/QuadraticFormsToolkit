from math import sqrt, ceil
def diag(a,b,c,k):
    v = max(ceil(sqrt(k)),2)
    for x in range(v):
        for y in range(v):
            for z in range(v):
                # print(x,y,z)
                if a*x**2+b*y**2+c*z**2==k:
                    return True
    return False

def diagonal(a,b,c):
    for k in range(15):
        if not diag(a,b,c,k):
            print(k,"fails")
            return False
    return True

# diagonal(1,2,3)
# print(diag(1,1,3,6**(2*3+1)))
print(diag(1,2,5,10))
