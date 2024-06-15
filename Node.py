from time import sleep
from Network import Network


class Node:
    def __init__(
        self, 
        balance, 
        transactions_memory_pool=None, 
        block_memory_pool=None,
        created_blocks=None,
    ):
        self.id = generate_node_id()
        self.balance = balance
        self.transactions_memory_pool = transactions_memory_pool if transactions_memory_pool is not None else {}
        self.block_memory_pool = block_memory_pool if block_memory_pool is not None else {}
        self.created_blocks = created_blocks if created_blocks is not None else []
    
    
    def broadcast_transaction(self, transaction):
        
        from Configuration import GeneralConfiguration
        
        sleep(GeneralConfiguration.transaction_propagation_delay) 
        
        for node in Network.nodes.values():
            node.transactions_memory_pool[transaction.id] = transaction
            
        print(f"Node {self.id} has broadcasted transaction {transaction.id} to the network.\n")
        return transaction
    
    
    def broadcast_block(self, block):
        from Configuration import GeneralConfiguration
        
        sleep(GeneralConfiguration.block_propagation_delay)
        
        for node in Network.nodes.values():
            node.block_memory_pool[block.hash] = block
            
        print(f"\nNode {self.id} has broadcasted block {block.hash} to the network. It contains {len(block.transactions)} transactions.\n")
        return block
        
        
    def __eq__(self, other):
        if not isinstance (other, Node):
            return False
        return self.id == other.id 
    
    
    
def generate_node_id():
    
    import os

    random_bytes = os.urandom(6)
    node_id_in_hex = random_bytes.hex()
    return node_id_in_hex
    
    
        
            