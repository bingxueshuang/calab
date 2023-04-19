import ecdsa
from ecdsa import SigningKey, VerifyingKey, NIST384p

# @return sk, pk : private-public key pair in hex format
def generate_key():
	sk = SigningKey.generate(curve=NIST384p)
	vk = sk.get_verifying_key()
	return sk.to_string().hex(), vk.to_string().hex()

# @param sk_hex : private key in hex format
# @param message : bytes data to be signed
# @return sign : ecdsa digital signature in hex format
def sign_message(sk_hex, message):
	sk_bytes = bytes.fromhex(sk_hex)
	sk = SigningKey.from_string(sk_bytes, curve=NIST384p)
	signature = sk.sign(message)
	return signature.hex()

# @param vk_hex : public key in hex format
# @param signature : ecdsa digital signature in hex format
# @param message : bytes data to be verified
# @return ok : bool whether signature is valid or not
def verify(vk_hex, signature, message):
	vk_bytes = bytes.fromhex(vk_hex)
	vk = VerifyingKey.from_string(vk_bytes, curve=NIST384p)
	signature_bytes = bytes.fromhex(signature)
	return vk.verify(signature_bytes, message)

sk, pk = generate_key() # key pair
msg = input().encode() # input data
sign = sign_message(sk, msg) # digital signature
print(sign)
print(verify(pk, sign, msg)) # if signature is valid
