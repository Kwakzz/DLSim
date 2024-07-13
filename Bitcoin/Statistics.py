from Statistics import print_average_latency, print_throughput, print_average_block_time

hash_rates = []


def print_bitcoin_statistics():
    print_total_hashpower()
    print_average_hash_rate()
    print_throughput()
    print_average_latency()
    print_average_block_time()
    
    
def get_total_hashpower():
    from Network import Network
    
    total_hashpower = sum(node.hashpower for node in Network.nodes.values()) 
    return total_hashpower


def print_total_hashpower():
    print(f"Network total hashpower: {get_total_hashpower()}")
    
    
def get_average_hash_rate():
    
    average_hash_rate = sum(hash_rates)/len(hash_rates)
    average_hash_rate = round(average_hash_rate, 4)
    return average_hash_rate


def get_hash_rate(hash_attempts, elapsed_time):
    return hash_attempts/elapsed_time


def record_hash_rate (hash_rate):
    hash_rates.append(hash_rate)
    

def print_average_hash_rate():
    
    from Bitcoin.Consensus import Consensus as PoW
    
    print(f"Network hash rate: {get_average_hash_rate()} hashes/second")
    
    