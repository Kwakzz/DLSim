from Network import Network
from Block import Block
from Configuration import Configuration

class Node:
    def __init__(self, id, balance=0):
        self.id = id
        self.balance = balance
        self.blockchain = []
        self.memory_pool = []
        
    def is_equal(node1, node2):
        return node1.id == node2.id
            
    def generate_block(self):
        if Network.memory_pool:
            accumulated_transaction_gas = 0
            transaction_count = 0
            length_of_blockchain = len(self.blockchain)
            block = Block(id=length_of_blockchain)
            block.timestamp = Configuration.current_time
            
            while accumulated_transaction_gas < Configuration.block_limit:
                current_transaction = Network.memory_pool[transaction_count]
                accumulated_transaction_gas += current_transaction.gas
                block.transactions.append(current_transaction)

                transaction_count += 1             
                  
            return block
                
    
    def propagate_block(self):
        for node_count in range(Configuration.no_of_nodes):
            current_node = Network.nodes[node_count]
            current_node.blockchain.append(self)
            