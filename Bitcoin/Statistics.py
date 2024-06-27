from Configuration import BitcoinConfiguration, GeneralConfiguration
from Statistics import print_latency, print_throughput, record_latency, record_throughput, record_average_block_time, print_average_block_time

hash_rates = []

 
def record_bitcoin_statistics():
    record_bitcoin_network_hash_rate()
    record_throughput()
    record_latency()
    record_average_block_time()


def print_bitcoin_statistics():
    print("\nSTATISTICS:\n")
    print_bitcoin_network_total_hashpower()
    print_bitcoin_network_hash_rate()
    print_throughput()
    print_latency()
    print_average_block_time()


def print_bitcoin_network_total_hashpower():
    
    from Network import Network
    
    total_hashpower = sum(node.hashpower for node in Network.nodes.values()) 
    print(f"Network total hashpower: {total_hashpower}")
    
    
def get_bitcoin_network_hash_rate():
    
    from Bitcoin.Consensus import Consensus as PoW
     
    hash_rate = PoW.hash_attempts/BitcoinConfiguration.elapsed_time_for_mining_round
    return hash_rate


def record_bitcoin_network_hash_rate ():
    hash_rates.append(get_bitcoin_network_hash_rate())
    

def print_bitcoin_network_hash_rate():
    
    from Bitcoin.Consensus import Consensus as PoW
     
    hash_rate = PoW.hash_attempts/BitcoinConfiguration.elapsed_time_for_mining_round
    print(f"Network hash rate: {hash_rate} hashes/second")
    
    