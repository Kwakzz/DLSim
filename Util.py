import secrets


def generate_nonce():
    return str(secrets.randbelow(2**32))


def sha256_hash(data):
    import hashlib
    
    encoded_data = data.encode()
    hasher = hashlib.sha256(encoded_data)
    hex_digest = hasher.hexdigest() # string representation of hash in hex
    return hex_digest
                
                
def print_chain():
    
    from Network import Network
    
    random_node = next(iter(Network.nodes.values()))
    
    print ("Blockchain:", end=" ")
    
    print ("[", end="")
    for block in random_node.blockchain:
        print(block.hash, end="->")
    print("]")
    
    
def convert_seconds_to_minutes(time):
    return round(time/60, 2)


def convert_bytes_to_megabytes(size):
    return size/2**20


# Convert to %Y-%m-%d %H:%M:%S  
def format_datetime(datetime):
    return datetime.strftime("%Y-%m-%d %H:%M:%S")