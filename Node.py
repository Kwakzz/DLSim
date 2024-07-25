import random
from time import sleep
from Network import Network
from Util import generate_id, transaction_delay


class Node:
    def __init__(
        self, 
        balance
    ):
        self.id = generate_id()
        self.balance = balance
        self.transactions_memory_pool = {}
        self.block_memory_pool = {}
    
    
    def broadcast_transaction(self, transaction):
        
        print(f"{self.id} is broadcasting transaction {transaction.id} to the network.\n")
        
        transaction_delay()
        
        for node in Network.nodes.values():
            node.transactions_memory_pool[transaction.id] = transaction
        
        # print(f"Node {self.id} has broadcasted transaction {transaction.id} to the network.\n")
        return transaction
    
    
    def broadcast_transaction_without_delay(self, transaction):
                        
        for node in Network.nodes.values():
            node.transactions_memory_pool[transaction.id] = transaction
            
        # print(f"Node {self.id} has broadcasted transaction {transaction.id} to the network.\n")
        return transaction
    
    
    def broadcast_block(self, block):
        from Configuration import GeneralConfiguration
        
        propagation_delay = GeneralConfiguration.calculate_block_propagation_delay(len(Network.nodes), block.size)
        sleep(propagation_delay)
        
        for node in Network.nodes.values():
            node.block_memory_pool[block.hash] = block
        
        print(f"\nNode {self.id} has broadcasted block {block.hash} to the network. It contains {len(block.transactions)} transactions.\n")
        print(f"There was a propagation delay of {propagation_delay} seconds.")
        return block
        
        
    def buy_coins(self):
        amount = random.randrange(10000, 100000)
        self.balance += amount
        
        
    def __eq__(self, other):
        if not isinstance (other, Node):
            return False
        return self.id == other.id 

            
            
def update_balances():
    
    for node in Network.nodes.values():
        node.buy_coins()