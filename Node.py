from Block import Block
from Configuration import GeneralConfiguration, generate_node_id
from Network import Network


class Node:
    def __init__(self, balance=0, blockchain=[], transactions_memory_pool={}, block_memory_pool={}):
        self.id = generate_node_id()
        self.balance = balance
        self.blockchain=blockchain
        self.transactions_memory_pool=transactions_memory_pool
        self.block_memory_pool=block_memory_pool 
    
    def broadcast_transaction(self, transaction):
        for node in Network.nodes.values():
            node.transactions_memory_pool[transaction.id] = transaction
        print("Node {} has broadcasted transaction {} to the network\n".format(self.id, transaction.id))
    
    def broadcast_block(self, block):
        for node in Network.nodes.values():
            node.block_memory_pool[block.hash] = block
        print("\nNode {} has broadcasted block {} to the network. It contains {} transactions.\n".format(self.id, block.id, len(block.transactions)))
        return block
        
    def __eq__(self, other):
        if not isinstance (other, Node):
            return False
        return self.id == other.id 
    
    def __str__(self):
        node_type = "Full"
        if not self.blockchain:
            node_type = "Lightweight"
        return f"Node(ID: {self.id}, Balance: {self.balance}, Type: {node_type})\n"
        
            