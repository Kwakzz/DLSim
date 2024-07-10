import random
from time import sleep
from Network import Network


class Node:
    def __init__(
        self, 
        balance, 
        transactions_memory_pool=None, 
        block_memory_pool=None,
    ):
        self.id = generate_node_id()
        self.balance = balance
        self.transactions_memory_pool = transactions_memory_pool if transactions_memory_pool is not None else {}
        self.block_memory_pool = block_memory_pool if block_memory_pool is not None else {}
    
    
    def broadcast_transaction(self, transaction):
        
        from Configuration import GeneralConfiguration, BitcoinConfiguration, EthereumConfiguration
        
        transaction_propagation_delay = None 
        if GeneralConfiguration.selected_platform == "Bitcoin":
            transaction_propagation_delay = random.choice(BitcoinConfiguration.transaction_propagation_delay)
        if GeneralConfiguration.selected_platform == "Ethereum":
            transaction_propagation_delay = random.choice(EthereumConfiguration.transaction_propagation_delay)
        
        sleep(transaction_propagation_delay) 
        
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
    
    
    
def generate_node_id():
    
    import os

    random_bytes = os.urandom(6)
    node_id_in_hex = random_bytes.hex()
    return node_id_in_hex
            
            
def update_balances():
    
    for node in Network.nodes.values():
        node.buy_coins()