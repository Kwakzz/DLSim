import random
from Configuration import GeneralConfiguration
from Util import convert_seconds_to_minutes


def generate_overall_statistics():
    from Ethereum.Statistics import print_ethereum_statistics
    from Bitcoin.Statistics import print_bitcoin_statistics
    from Fabric.Statistics import print_fabric_statistics
    
    print("\nOVERALL STATISTICS:\n")

    if GeneralConfiguration.selected_platform == "Ethereum":
        print_ethereum_statistics()
        
    if GeneralConfiguration.selected_platform == "Bitcoin":
        print_bitcoin_statistics()
        
    if GeneralConfiguration.selected_platform == "Fabric":
        print_fabric_statistics()
        
        
def generate_current_statistics():
    from Ethereum.Statistics import print_ethereum_statistics
    from Bitcoin.Statistics import print_bitcoin_statistics
    from Fabric.Statistics import print_fabric_statistics
    
    print("\nCURRENT STATISTICS:\n")

    if GeneralConfiguration.selected_platform == "Ethereum":
        print_ethereum_statistics()
        
    if GeneralConfiguration.selected_platform == "Bitcoin":
        print_bitcoin_statistics()
        
    if GeneralConfiguration.selected_platform == "Fabric":
        print_fabric_statistics()


# GENERAL
    
def get_throughput():
    
    random_node = None
    
    if GeneralConfiguration.selected_platform == "Ethereum" or GeneralConfiguration.selected_platform == "Bitcoin":
        from Network import Network
        random_node = Network.get_random_node()
        
    if GeneralConfiguration.selected_platform == "Fabric":
        from Fabric.Network import Network as FabricNetwork
        random_node = FabricNetwork.get_random_peer()
        
    transaction_count = 0
    
    for block in random_node.blockchain:
        transaction_count += block.transaction_count
    
    simulation_time = (GeneralConfiguration.simulation_end_time - GeneralConfiguration.simulation_start_time).total_seconds()
    simulation_time_in_minutes = convert_seconds_to_minutes(simulation_time)
    throughput = transaction_count/simulation_time
    throughput = round(throughput, 2)
    print(f"{transaction_count} transactions processed in {simulation_time_in_minutes} minutes.")
    
    return throughput
    
    
def print_throughput():
    throughput = get_throughput()
    print (f"Network throughput: {throughput} transactions/second")
    
    
def get_average_latency():
    
    random_node = None
    
    if GeneralConfiguration.selected_platform == "Ethereum" or GeneralConfiguration.selected_platform == "Bitcoin":
        from Network import Network
        random_node = Network.get_random_node()
        
    if GeneralConfiguration.selected_platform == "Fabric":
        from Fabric.Network import Network as FabricNetwork
        random_node = FabricNetwork.get_random_peer()
        
    sum_of_latencies = 0
    transaction_count = 0
            
    if len(random_node.blockchain) > 1:
        for block in random_node.blockchain:
            if len(list(block.transactions.values())) != 0:
                for transaction in block.transactions.values():
                    transaction_count += 1
                    latency = (transaction.confirmation_time - transaction.timestamp).total_seconds()
                    sum_of_latencies += latency
                
    average_latency = 0
       
    if transaction_count != 0:     
        average_latency = sum_of_latencies/transaction_count
        average_latency_in_minutes = convert_seconds_to_minutes(average_latency)
        average_latency = round(average_latency_in_minutes, 2)
            
    return average_latency
    
    
def print_average_latency():
    latency = get_average_latency()
    print (f"Network average latency is: {latency} minutes.")
    
    
def get_recent_block_time():
    
    random_node = None
    
    if GeneralConfiguration.selected_platform == "Ethereum" or GeneralConfiguration.selected_platform == "Bitcoin":
        from Network import Network
        random_node = Network.get_random_node()
        
    if GeneralConfiguration.selected_platform == "Fabric":
        from Fabric.Network import Network as FabricNetwork
        random_node = FabricNetwork.get_random_peer()
     
    if len(random_node.blockchain) < 2:
        print("Blockchain must contain at least two blocks to calculate average block time.")
        return 0

    recent_block = random_node.blockchain[-1]
    second_recent_block = random_node.blockchain[-2]
    block_time = (recent_block.timestamp - second_recent_block.timestamp).total_seconds()
    block_time_in_minutes = convert_seconds_to_minutes(block_time)
    block_time = round(block_time_in_minutes, 2)
    
    return block_time
    
    
def get_average_block_time():
    
    random_node = None
    
    if GeneralConfiguration.selected_platform == "Ethereum" or GeneralConfiguration.selected_platform == "Bitcoin":
        from Network import Network
        random_node = Network.get_random_node()
        
    if GeneralConfiguration.selected_platform == "Fabric":
        from Fabric.Network import Network as FabricNetwork
        random_node = FabricNetwork.get_random_peer()
            
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
    average_block_time_in_minutes = convert_seconds_to_minutes(average_block_time)
    average_block_time = round(average_block_time_in_minutes, 4)
    return average_block_time
    
    
def print_average_block_time():
    average_block_time = get_average_block_time()
    print(f"Average block time is {average_block_time} minutes")