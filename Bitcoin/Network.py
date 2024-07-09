import random
from time import time
from Network import Network as BaseNetwork
from Configuration import BitcoinConfiguration, GeneralConfiguration
from Statistics import get_average_block_time, get_recent_block_time

class Network (BaseNetwork):
    
    current_difficulty = BitcoinConfiguration.INITIAL_DIFFICULTY_TARGET
    
    @staticmethod
    def add_node():
        from Bitcoin.Node import Node as BitcoinNode
        
        initial_balance = random.randrange(GeneralConfiguration.MINIMUM_INITIAL_BALANCE, GeneralConfiguration.MAXIMUM_INITIAL_BALANCE)
            
        hashpower_class_no = random.randrange(1, 4) 
        hashpower_class = None
        
        if hashpower_class_no == 1:
            hashpower_class = BitcoinConfiguration.LOW_HASHPOWER
        elif hashpower_class_no == 2:
            hashpower_class = BitcoinConfiguration.MEDIUM_HASHPOWER
        elif hashpower_class_no == 3:
            hashpower_class = BitcoinConfiguration.HIGH_HASHPOWER
        
        hashpower = hashpower_class
        
        node = BitcoinNode(balance=initial_balance, hashpower=hashpower)
        Network.nodes[node.id] = node
        print(node)
    

    @staticmethod
    def verify_block(block):
        
        for node in Network.nodes.values():
            node.block_memory_pool.pop(block.hash)
        
        if block.is_valid():
            return True
        
        return False
    
    
    @staticmethod
    def calculate_new_difficulty():
        return Network.find_block_time_ratio * Network.current_difficulty
    
    
    @staticmethod
    def set_new_difficulty():
        
        recent_block_time = get_recent_block_time()
        print(f"Recent block time was {recent_block_time} minutes.")
                
        random_node_item = random.choice(list(Network.nodes.items()))
        random_node = random_node_item[1]
        
        blockchain_length = len(random_node.blockchain)
        if blockchain_length % BitcoinConfiguration.DIFFICULTY_ADJUSTMENT_INTERVAL == 0:
            Network.current_difficulty = Network.calculate_new_difficulty()


    @staticmethod
    def calculate_target(difficulty):
        return BitcoinConfiguration.INITIAL_TARGET / difficulty
    
    
    # expected block time/actual block time
    @staticmethod
    def find_block_time_ratio(): 
        cumulative_expected_block_time = BitcoinConfiguration.DIFFICULTY_ADJUSTMENT_INTERVAL * BitcoinConfiguration.TARGET_BLOCK_TIME
        unit_actual_block_time = get_average_block_time()
        cumulative_actual_block_time = BitcoinConfiguration.DIFFICULTY_ADJUSTMENT_INTERVAL * unit_actual_block_time
        ratio = cumulative_expected_block_time/cumulative_actual_block_time
        return ratio
    
    
                