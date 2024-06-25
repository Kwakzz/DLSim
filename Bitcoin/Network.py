import random
from Network import Network as BaseNetwork
from Configuration import BitcoinConfiguration, GeneralConfiguration

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
        if BitcoinConfiguration.prev_elapsed_time_for_mining_round > 0:
            ratio = BitcoinConfiguration.current_total_block_time / BitcoinConfiguration.target_block_time
            BitcoinConfiguration.difficulty_target = BitcoinConfiguration.difficulty_target//ratio
            BitcoinConfiguration.base_pow_time *= ratio
            print(f"Adjusted difficulty: {BitcoinConfiguration.difficulty}.\n")
            print(f"Adjusted base PoW time: {BitcoinConfiguration.base_pow_time} seconds.\n")  



    @staticmethod
    def verify_block(block, miner):
        
        if block.is_valid():
            
            block.add_to_chain()
                
            for node in Network.nodes.values():
                node.block_memory_pool.pop(block.hash)
                
            for transaction in block.transactions.values():
                transaction.finalize(miner)
                
            return True
        
        return False
                
    
    @staticmethod    
    def verify_broadcasted_blocks(broadcasted_blocks, miners):
        
        for i in range (len(broadcasted_blocks)):
            
            block = broadcasted_blocks[i]
            miner = miners[i]
            
            if Network.verify_block(block, miner):
                break   