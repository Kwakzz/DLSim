import random
from time import time
from Network import Network as BaseNetwork
from Configuration import BitcoinConfiguration, GeneralConfiguration
from Statistics import get_average_block_time, get_recent_block_time
from Util import convert_seconds_to_minutes

class Network (BaseNetwork):
    
    @staticmethod
    def add_node():
        from Bitcoin.Node import Node as BitcoinNode
        
        initial_balance = random.randrange(GeneralConfiguration.minumum_initial_balance, GeneralConfiguration.maximum_initial_balance)
            
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
    def adjust_difficulty_target():
        
        from Bitcoin.Consensus import Consensus as PoW
        
        recent_block_time = get_recent_block_time()
        print(f"Recent block time was {recent_block_time} seconds or {convert_seconds_to_minutes(recent_block_time)} minutes.")
                
        random_node_item = random.choice(list(Network.nodes.items()))
        random_node = random_node_item[1]
        
        if PoW.solve_time > 0 and len(random_node.blockchain) > 2:
            
            ratio = PoW.solve_time/BitcoinConfiguration.target_block_time
            if ratio > 1:
                BitcoinConfiguration.difficulty_target = max(1, BitcoinConfiguration.difficulty_target-1)
            else:
                BitcoinConfiguration.difficulty_target+=1
            
            # BitcoinConfiguration.base_pow_time *= ratio
            
            print(f"Adjusted difficulty: {BitcoinConfiguration.difficulty_target}.")
            # print(f"Adjusted base PoW time: {BitcoinConfiguration.base_pow_time} seconds.\n")
        else:
            print("Recent block time is zero or negative, or only one block has been appended to the chain difficulty adjustment skipped.")


    @staticmethod
    def verify_block(block):
        
        for node in Network.nodes.values():
            node.block_memory_pool.pop(block.hash)
        
        if block.is_valid():
            return True
        
        return False
                