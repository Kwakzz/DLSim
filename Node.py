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
            
    def generate_block(self):
        if self.memory_pool:
            accumulated_transaction_gas = 0
            transaction_count = 0
            length_of_blockchain = len(self.blockchain)
            block = Block(id=length_of_blockchain, miner_id=self.id)
            
            block.timestamp = Configuration.current_time
            block.miner_id = self.id
            
            # Ensure transaction_count is within the bounds of memory_pool length
            while transaction_count < len(self.memory_pool) and accumulated_transaction_gas < Configuration.block_limit:
                current_transaction = self.memory_pool[transaction_count]
                accumulated_transaction_gas += current_transaction.gas
                block.transactions.insert(current_transaction.id, current_transaction)

                transaction_count += 1             
                
            self.block_memory.insert(block.id, block)
            print("\nBlock {} has been generated. It stores {} transactions".format(block.id, len(block.transactions)))
            return block

                
    
    def propagate_block(self, block):
        from Network import Network
        self.block_memory.remove(block)
        for node_count in range(Configuration.no_of_nodes):
            current_node = Network.nodes[node_count]
            current_node.blockchain.insert(block.id, block)
        print("\nBlock {} has been added to the blockchain".format(block.id))
            