from Configuration import BitcoinConfiguration, GeneralConfiguration

hash_rates = []
throughputs = []
latencies = []


 # BITCOIN 
 
def record_bitcoin_statistics():
    record_bitcoin_network_hash_rate()
    record_throughput()
    record_latency()


def print_bitcoin_statistics():
    print("\nSTATISTICS:\n")
    print_bitcoin_network_total_hashpower()
    print_bitcoin_network_hash_rate()
    print_throughput()
    print_latency()


def print_bitcoin_network_total_hashpower():
    
    from Network import Network
    
    total_hashpower = sum(node.hashpower for node in Network.nodes.values()) 
    print(f"Network total hashpower: {total_hashpower}\n")
    
    
def get_bitcoin_network_hash_rate():
    
    from Bitcoin.Consensus import Consensus as PoW
     
    hash_rate = PoW.hash_attempts/BitcoinConfiguration.current_elapsed_time_for_mining_round
    return hash_rate


def record_bitcoin_network_hash_rate ():
    hash_rates.append(get_bitcoin_network_hash_rate())
    

def print_bitcoin_network_hash_rate():
    
    from Bitcoin.Consensus import Consensus as PoW
     
    hash_rate = PoW.hash_attempts/BitcoinConfiguration.current_elapsed_time_for_mining_round
    print(f"Network hash rate: {hash_rate} hashes/second")
    
    

# GENERAL
    
def get_throughput():
    elapsed_time = GeneralConfiguration.transaction_batch_end_time - GeneralConfiguration.transaction_batch_start_time
    throughput = GeneralConfiguration.processed_transaction_count/elapsed_time
    return throughput
    

def record_throughput():
    throughputs.append(get_throughput())
    
    
def print_throughput():
    throughput = get_throughput()
    print (f"Network throughput: {throughput} transactions/second")
    
    
def get_latency():
    latency = GeneralConfiguration.transaction_batch_end_time - GeneralConfiguration.transaction_batch_start_time
    return latency


def record_latency():
    latencies.append(get_latency())
    
    
def print_latency():
    latency = get_latency()
    print (f"Network latency is: {latency} seconds.")


