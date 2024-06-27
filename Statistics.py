import random
from Configuration import BitcoinConfiguration, GeneralConfiguration
from Network import Network

transaction_latencies = []


def generate_statistics():
    from Ethereum.Statistics import print_ethereum_statistics
    from Bitcoin.Statistics import print_bitcoin_statistics

    if GeneralConfiguration.selected_platform == "Ethereum":
        print_ethereum_statistics()
        
    if GeneralConfiguration.selected_platform == "Bitcoin":
        print_bitcoin_statistics()
        

# GENERAL
    
def get_throughput():
    
    random_node_item = random.choice(list(Network.nodes.items()))
    random_node = random_node_item[1]
    transaction_count = 0
    
    for block in random_node.blockchain:
        transaction_count += len(block.transactions)
    
    simulation_time = (GeneralConfiguration.simulation_end_time - GeneralConfiguration.simulation_start_time).total_seconds()
    throughput = transaction_count/simulation_time
    throughput = round(throughput, 2)
    
    return throughput
    
    
def print_throughput():
    throughput = get_throughput()
    print (f"Network throughput: {throughput} transactions/second")
    
    
def get_average_latency():
    
    random_node_item = random.choice(list(Network.nodes.items()))
    random_node = random_node_item[1]
    
    for block in random_node.blockchain:
        for transaction in block.transactions.values():
            latency = (transaction.confirmation_time - transaction.timestamp).total_seconds()
            record_latency(latency)
            
    average_latency = sum(transaction_latencies)/len(transaction_latencies)
    average_latency = round(average_latency, 2)
    
    return average_latency


def record_latency(latency):
    transaction_latencies.append(latency)
    
    
def print_average_latency():
    latency = get_average_latency()
    print (f"Network average latency is: {latency} seconds.")
    
    
def get_recent_block_time():
    
    random_node_item = random.choice(list(Network.nodes.items()))
    random_node = random_node_item[1]
    
    if len(random_node.blockchain) < 2:
        print("Blockchain must contain at least two blocks to calculate average block time.")
        return 0

    recent_block = random_node.blockchain[-1]
    second_recent_block = random_node.blockchain[-2]
    block_time = (recent_block.timestamp - second_recent_block.timestamp).total_seconds()
    block_time = round(block_time, 2)
    
    return block_time
    
    
    
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
        
    average_block_time = cumulative_block_time/no_of_block_times
    average_block_time = round(average_block_time, 4)
    return average_block_time
    
    
def print_average_block_time():
    average_block_time = get_average_block_time()
    print(f"Average block time is {average_block_time} seconds")
        
        


