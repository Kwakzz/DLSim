from Configuration import BitcoinConfiguration, GeneralConfiguration

hash_rates = []
throughputs = []


def record_bitcoin_statistics():
    record_hash_rate()
    record_throughput()


def print_bitcoin_statistics():
    print_bitcoin_network_total_hashpower()
    print_bitcoin_network_hash_rate()
    print_throughput()


def print_bitcoin_network_total_hashpower():
    
    from Network import Network
    
    total_hashpower = sum(node.hashpower for node in Network.nodes.values()) 
    print(f"Network total hashpower: {total_hashpower}\n.")
    
    
def calculate_bitcoin_network_hash_rate():
    
    from Bitcoin.Consensus import Consensus as PoW
     
    hash_rate = PoW.hash_attempts/BitcoinConfiguration.current_elapsed_time_for_mining_round
    return hash_rate


def record_hash_rate ():
    hash_rates.append(calculate_bitcoin_network_hash_rate())
    

def print_bitcoin_network_hash_rate():
    
    from Bitcoin.Consensus import Consensus as PoW
     
    hash_rate = PoW.hash_attempts/BitcoinConfiguration.current_elapsed_time_for_mining_round
    print(f"Network hash rate: {hash_rate} TH/s.\n")
    
    
    
def calculate_throughput():
    elapsed_time = GeneralConfiguration.transaction_batch_end_time - GeneralConfiguration.transaction_batch_start_time
    throughput = GeneralConfiguration.processed_transaction_count/elapsed_time
    return throughput
    

def record_throughput():
    throughputs.append(calculate_throughput())
    
    
def print_throughput():
    throughput = calculate_throughput()
    print (f"Network throughput is: {throughput} t/s.\n")