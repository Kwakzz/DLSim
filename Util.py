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
    if BitcoinConfiguration.prev_elapsed_time_for_mining_round > 0:
        ratio = BitcoinConfiguration.current_elapsed_time_for_mining_round / BitcoinConfiguration.target_block_time
        BitcoinConfiguration.difficulty_target = BitcoinConfiguration.difficulty_target//ratio
        BitcoinConfiguration.base_pow_time *= ratio
        print(f"Adjusted difficulty: {BitcoinConfiguration.difficulty}.\n")
        print(f"Adjusted base PoW time: {BitcoinConfiguration.base_pow_time} seconds.\n")
                
                
def print_chain():
    
    from Network import Network
    
    random_node = next(iter(Network.nodes.values()))
    
    print ("Blockchain:", end=" ")
    
    print ("[", end="")
    for block in random_node.blockchain:
        print(block.hash, end="->")
    print("]")