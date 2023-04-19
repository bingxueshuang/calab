import random
import hashlib

p=127
g=2

xa=random.randint(1,p)
ya=pow(g,xa,p)

k=random.randint(1,p)
r=pow(g,k,p)

M=50

e=int(hashlib.sha256((str(r)+str(M)).encode()).hexdigest(),16)%p
s=k-xa*e

rv=(pow(g,s,p)*pow(ya,e,p))%p
ev=int(hashlib.sha256((str(rv)+str(M)).encode()).hexdigest(),16)%p

if e==ev:
    print("Valid")
else:
    print("Invalid")