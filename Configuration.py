import random
import secrets
import string
import time
import threading

def generate_random_32_bit_number():
    return secrets.randbelow(2**32)

def sha256_hash(data):
    import hashlib
    
    encoded_data = data.encode()
    hasher = hashlib.sha256(encoded_data)
    hex_digest = hasher.hexdigest() # string representation of hash in hex
    return hex_digest

def generate_block_hash(block):
    
    number_of_transactions = len(block.transactions)
    transaction_hashes = []
    paired_transaction_hashes = []
    
    for transaction in block.transactions.values():
        transaction_hashes.append(transaction.id)
        
    if (number_of_transactions % 2 == 1):
        transaction_hashes.append(transaction_hashes[-1]) # duplicate final hash if list is odd-numbered
        
    for i in range (0, len(transaction_hashes)-1, 2):
        paired_transaction_hash = sha256_hash(transaction_hashes[i] + transaction_hashes[i+1])
        paired_transaction_hashes.append(paired_transaction_hash)
    
    separator = ""
    block.hash = separator.join([string for hash in paired_transaction_hashes])
    return block.hash
        
def generate_node_id():
    import os

    random_bytes = os.urandom(6)
    node_id_in_hex = random_bytes.hex()
    return node_id_in_hex

def set_bitcoin_transaction_fee(transaction_size):
    ((transaction_size/1000) * no_of_pending_transactions) * 0.00005
    
def is_pow_found(block_hash):
    return block_hash.startswith("0"*BitcoinConfiguration.difficulty_target)

no_of_pending_transactions = 0


class GeneralConfiguration:
        
    no_of_runs = 3
    
    no_of_transactions_per_round = 30
    
    maximum_initial_balance = 200
    minumum_initial_balance = 10
    
    no_of_nodes = 50
        
    selected_platform = "Bitcoin"


class EthereumConfiguration:
        
    transaction_gas_limit = 21000 # maximum amount you are willing to consume on a transaction. Standard transaction gas limit is 21000 units of gas
    block_gas_limit = 210000
    transaction_gas = 50 # measures the computational effort required to execute a transaction.
    base_fee = 10 # minimum transaction fee in Ethereum
    target_size = 15000000 # the amount of cumulative gas a block takes
    
    from Configuration import GeneralConfiguration
    no_of_nodes_staking = random.randrange(GeneralConfiguration.no_of_nodes/2, GeneralConfiguration.no_of_nodes+1)
    

class BitcoinConfiguration:
    block_size_limit = 1000 # actual block size limit for Bitcoin is 1MB. 1000 here represents 1000KB, which is approximately 1MB.
    maximum_hashpower = 100
    minimum_hashpower = 20
    difficulty_target = 4
    no_of_miners = 3
    