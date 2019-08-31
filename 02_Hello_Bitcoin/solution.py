from secp256k1 import *
import hashlib
from Crypto.Hash import RIPEMD
import base58check

print('Curve:', curve.name)

# 0. Having a private ECDSA key
#private_key = 0x18e14a7b6a307f426a94f8114701e7c8e774e7f9a47e2c2035db29a206321725
private_key = 94176137926187438630526725483965175646602324181311814940191841477114099191175
#private_key = 5
compressed = False
print("private key:", hex(private_key))

# 1. Taking the corresponding public key generated with it
public_key_point = scalar_mult(private_key,curve.g)
print("public key: (0x{:x}, 0x{:x})".format(*public_key_point))

if compressed:
    public_key = ""
    if public_key[0] %2:
        public_key += '03'
    else:
        public_key += '02'

    public_key += hex(public_key_point[0])[2:]

    print("compressed public key: {:s}".format(public_key))


else:
    public_key = "04"
    public_key += hex(public_key_point[0])[2:] + hex(public_key_point[1])[2:]

# 2. Perform SHA-256 hashing on the public key

sha256_hash = hashlib.sha256(bytearray.fromhex(public_key)).hexdigest()

print("sha256 hash: {:s}".format(sha256_hash))


# 3. Perform RIPEMD-160 hashing on the result of SHA-256

h = RIPEMD.new()
h.update(bytearray.fromhex(sha256_hash))
ripemd160_hash = h.hexdigest()

print("ripemd160 hash: {:s}".format(ripemd160_hash))


# 4. Add version type in the front of RIPEMD-160 hash

ripemd160_hash = '00' + ripemd160_hash
print("ripemd160 hash with version: {:s}".format(ripemd160_hash))


# 5. Perform SHA-256 hash on the extended RIPEMD-160 result

sha256_hash2 = hashlib.sha256(bytearray.fromhex(ripemd160_hash)).hexdigest()
print("sha256 hash again: {:s}".format(sha256_hash2))

# 6. Perform SHA-256 hash on the result of the previous SHA-256 hash

sha256_hash3 = hashlib.sha256(bytearray.fromhex(sha256_hash2)).hexdigest()
print("sha256 hash again again: {:s}".format(sha256_hash3))

# 7. Take the first 4 bytes of the second SHA-256 hash

address_checksum = sha256_hash3[:8]
print("address checksum: {:s}".format(address_checksum))


# 8. Add the 4 checksum bytes from stage 7 at the end of extended RIPEMD-160 hash from stage 4.

binary_address = ripemd160_hash + address_checksum
print("25byte binary bitcoin address: {:s}".format(binary_address))

# 9. Conver the result from a byte string into a base58 string using base58check encoding

formal_address = base58check.b58encode(bytes.fromhex(binary_address))
print("formal bitcoin address: {:s}".format(formal_address.decode('utf-8')))
