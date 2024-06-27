import random
from Configuration import BitcoinConfiguration, GeneralConfiguration
from Network import Network

throughputs = []
latencies = []
average_block_times = []
block_times = []

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
    
    
def get_recent_block_time():
    
    random_node_item = random.choice(list(Network.nodes.items()))
    random_node = random_node_item[1]
    
    if len(random_node.blockchain) < 2:
        print("Blockchain must contain at least two blocks to calculate average block time.")
        return 0

    recent_block = random_node.blockchain[-1]
    second_recent_block = random_node.blockchain[-2]
    
    return (recent_block.timestamp - second_recent_block.timestamp).total_seconds()
    
    
    
def get_average_block_time():
    
    random_node_item = random.choice(list(Network.nodes.items()))
    random_node = random_node_item[1]
    
    no_of_block_times = len(random_node.blockchain) - 1
    cumulative_block_time = 0
    
    if len(random_node.blockchain) < 2:
        print("Blockchain must contain at least two blocks to calculate average block time.")
        return 0
    
    for i in range (0, len(random_node.blockchain)-1):
        first_block = random_node.blockchain[i]
        second_block = random_node.blockchain[i+1]
        block_time = (second_block.timestamp - first_block.timestamp).total_seconds()
        cumulative_block_time += block_time
        
    return cumulative_block_time/no_of_block_times


def record_average_block_time():
    average_block_times.append(get_average_block_time)
    
    
def print_average_block_time():
    average_block_time = get_average_block_time()
    print(f"Average block time is {average_block_time} seconds")
        
        


