from Network import Network


class Node:
    def __init__(
        self, 
        balance, 
        transactions_memory_pool={}, 
        block_memory_pool={},
        created_blocks=[]
    ):
        self.id = generate_node_id()
        self.balance = balance
        self.transactions_memory_pool = transactions_memory_pool
        self.block_memory_pool = block_memory_pool 
        self.created_blocks = created_blocks
    
    
    def broadcast_transaction(self, transaction):
        for node in Network.nodes.values():
            node.transactions_memory_pool[transaction.id] = transaction
        print(f"Node {self.id} has broadcasted transaction {transaction.id} to the network\n")
    
    
    def broadcast_block(self, block):
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
    
    
        
            