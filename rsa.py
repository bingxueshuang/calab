# import hashlib

# @param a, b int : given two numbers
# @return gcd int : hcf of `a` and `b`
def gcd(a, b):
	if b == 0:
		return a
	else:
		return gcd(b, a%b)

# @param a, b int : given two numbers
# @return c int : inverse of `b` modulo `a`
def inv(a, b):
	for x in range(1, a):
		if (b*x) % a == 1:
			break
	return x

# @param msg int : message to decrypt
# @param pk (int,int) : public key `(n, e)`
# @return m int : decryption of `msg`
def decrypt(msg, pk):
	n, e = pk
	return (msg ** e) % n

# @param p, q int : two large prime numbers
# @return (sk, pk) ((int,int),(int,int)) : crypto key pair
def generate_key(p=11, q=7):
	n = p * q
	phi = (p-1) * (q-1)
	e = 2
	for i in range(phi):
		if gcd(phi, e) == 1:
			break
		e += 1
	d = inv(phi, e)
	return (n,d), (n,e)

# @param message int : message to encrypt
# @param sk (int,int) : private key n, d
def encrypt(message, sk):
	n, d = sk
	return (message ** d) % n

# m = int(hashlib.sha256(M.encode()).hexdigest(),16)
