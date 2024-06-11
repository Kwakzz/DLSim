from Configuration import GeneralConfiguration, BitcoinConfiguration
import random

class Network:
    
    nodes = {}
    
    def __init__(self):
        pass  
    
    
    def print_nodes():
        print("Network Nodes: ")
        for node in Network.nodes.values():
            print(node)
        
    
    def add_node():
        initial_balance = random.randrange(GeneralConfiguration.minumum_initial_balance, GeneralConfiguration.maximum_initial_balance)
        if GeneralConfiguration.selected_platform == "Bitcoin":
            from Bitcoin.Node import Node as BitcoinNode
            
            hashpower_class_no = random.randrange(1, 4) 
            hashpower_class = None
            
            if hashpower_class_no == 1:
                hashpower_class = random.choice(BitcoinConfiguration.low_power_hashpower)
            elif hashpower_class_no == 2:
                hashpower_class = random.choice(BitcoinConfiguration.medium_power_hashpower)
            elif hashpower_class_no == 3:
                hashpower_class = random.choice(BitcoinConfiguration.high_power_hashpower)
            
            hashpower = hashpower_class
            
            node = BitcoinNode(balance=initial_balance, hashpower=hashpower)
            Network.nodes[node.id] = node
            print(node)
        
    @staticmethod
    def initialize_network():
        print(f"Welcome to a simulation of the {GeneralConfiguration.selected_platform} blockchain network.\nNodes are joing the network...\n")
        for node_count in range(GeneralConfiguration.no_of_nodes):
            Network.add_node()
            
    
    def verify_block(block, miner):
        
        if block.is_valid():
            
            block.add_to_chain()
                
            for node in Network.nodes.values():
                node.block_memory_pool.pop(block.hash)
                
            for transaction in block.transactions.values():
                transaction.finalize(miner)
                
            return True
        
        return False
                
                
    def verify_broadcasted_blocks(broadcasted_blocks, miners):
        
        for i in range (len(broadcasted_blocks)):
            
            block = broadcasted_blocks[i]
            miner = miners[i]
            
            if Network.verify_block(block, miner):
                break
            
                                
def calculate_bitcoin_network_hash_rate(latest_no_of_hash_attempts_per_mining_round, latest_elapsed_time_for_mining_round):
    BitcoinConfiguration.hash_rate = latest_no_of_hash_attempts_per_mining_round/latest_elapsed_time_for_mining_round
    return BitcoinConfiguration.hash_rate


def print_bitcoin_network_hash_rate():
    print(f"Network hash rate: {BitcoinConfiguration.hash_rate} TH/s.\n")
     
    
def print_bitcoin_network_total_hashpower():
    total_hashpower = sum(node.hashpower for node in Network.nodes.values()) 
    print(f"Network total hashpower: {total_hashpower}\n.")
    
            
    
        
