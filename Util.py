import random
import secrets
import string


def generate_nonce():
    return str(secrets.randbelow(2**32))


def sha256_hash(data):
    import hashlib
    
    encoded_data = data.encode()
    hasher = hashlib.sha256(encoded_data)
    hex_digest = hasher.hexdigest() # string representation of hash in hex
    return hex_digest