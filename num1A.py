import hashlib

s = "DM Fall 2024 HW3"

hash_object = hashlib.sha256(s.encode('utf-8'))
hex_hash = hash_object.hexdigest()
binary_hash = bin(int(hex_hash, 16))[2:].zfill(256)
slices = [binary_hash[i:i + 32] for i in range(0, 256, 32)]
d = 0
for i in slices:
    d ^= int(i, 2)

w = d ^ 0x7613a0ca
print("Result w:", bin(w)[2:])
