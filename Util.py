import random
import secrets
import string
from Configuration import BitcoinConfiguration


def generate_nonce():
    return str(secrets.randbelow(2**32))


def sha256_hash(data):
    import hashlib
    
    encoded_data = data.encode()
    hasher = hashlib.sha256(encoded_data)
    hex_digest = hasher.hexdigest() # string representation of hash in hex
    return hex_digest


def adjust_difficulty_target():
    if BitcoinConfiguration.prev_elapsed_time_for_finding_pow is not None and BitcoinConfiguration.current_elapsed_time_for_finding_pow is not None:
        if BitcoinConfiguration.prev_elapsed_time_for_finding_pow >= BitcoinConfiguration.current_elapsed_time_for_finding_pow:
            BitcoinConfiguration.difficulty_target+=1
        else:
            if BitcoinConfiguration.difficulty_target >= 2:
                BitcoinConfiguration.difficulty_target-=1
                
                
def print_chain():
    
    from Network import Network
    
    random_node = next(iter(Network.nodes.values()))
    print(random_node.blockchain)