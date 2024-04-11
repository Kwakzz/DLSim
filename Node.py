from Block import Block
from Configuration import Configuration

class Node:
    def __init__(self, id, balance=0):
        self.id = id
        self.balance = balance
        self.blockchain = []
        self.memory_pool = [] #temporary storage for transactions
        self.block_memory = [] #temporary storage for blocks
        
    def is_equal(node1, node2):
        return node1.id == node2.id
            
    
    def propagate_block(self, block):
        from Network import Network
        self.block_memory.remove(block)
        for node_count in range(Configuration.no_of_nodes):
            current_node = Network.nodes[node_count]
            current_node.blockchain.insert(block.id, block)
        print("\nBlock {} has been added to the blockchain".format(block.id))
            