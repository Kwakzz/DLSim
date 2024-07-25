import hashlib
import random
from time import sleep
from Configuration import EthereumConfiguration, BitcoinConfiguration, GeneralConfiguration, coin_based_blockchains


def generate_id():    
    import os

    random_bytes = os.urandom(6)
    id_in_hex = random_bytes.hex()
    return id_in_hex


def sha256_hash(data):    
    if isinstance(data, str):
        data = data.encode('utf-8')
    return hashlib.sha256(data).hexdigest()
                
       
def double_256_hash(data):
    if isinstance(data, str):
        data = data.encode('utf-8')
        
    return hashlib.sha256(hashlib.sha256(data).digest()).hexdigest()
         
            
def print_chain():
    
    random_node = None
    
    if GeneralConfiguration.selected_platform in coin_based_blockchains:
        from Network import Network
        random_node = Network.get_random_node()
        
    if GeneralConfiguration.selected_platform == "Fabric":
        from Fabric.Network import Network
        random_node = Network.get_random_peer()
    
    print ("\nBlockchain:", end=" ")
    
    print ("[", end="")
    for block in random_node.blockchain:
        print(block.hash, end="->")
    print("]")
    
    
def get_chain_length():
    
    random_node = None
    
    if GeneralConfiguration.selected_platform in coin_based_blockchains:
        from Network import Network
        random_node = Network.get_random_node()
        
    if GeneralConfiguration.selected_platform == "Fabric":
        from Fabric.Network import Network
        random_node = Network.get_random_peer()
        
    blockchain_length = len(random_node.blockchain)
    return blockchain_length
    

    
def convert_seconds_to_minutes(time):
    return round(time/60, 2)


def convert_bytes_to_megabytes(size):
    return size/2**20


# Convert to %Y-%m-%d %H:%M:%S  
def format_datetime(datetime):
    return datetime.strftime("%Y-%m-%d %H:%M:%S")


def transaction_delay():
    transaction_propagation_delay = None 
    
    if GeneralConfiguration.selected_platform == "Bitcoin" or GeneralConfiguration.selected_platform == "Slimcoin":
        transaction_propagation_delay = random.choice(BitcoinConfiguration.transaction_propagation_delay)
    if GeneralConfiguration.selected_platform == "Ethereum":
        transaction_propagation_delay = random.choice(EthereumConfiguration.transaction_propagation_delay)
    
    sleep(transaction_propagation_delay) 