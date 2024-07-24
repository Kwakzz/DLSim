import random
from Bitcoin.Node import Node as BitcoinNode
from Configuration import SlimcoinConfiguration
from Slimcoin.BurnTransaction import BurnTransaction

class Node (BitcoinNode):
    
    def __init__(
        self, 
        balance, 
        hashpower,
    ):
        super().__init__(
            balance, 
            hashpower,
        )
        self.burn_transactions_memory_pool = {}
        
    
    def burn_coins(self, value):
        burn_transaction = BurnTransaction(
            value = value,
            sender_id = self.id
        )

        burn_transaction.set_hash()
        burn_transaction.set_multiplier()
        self.balance -= value
        
        self.broadcast_burn_transaction_without_delay(burn_transaction)
        
        print(burn_transaction)
        return burn_transaction
    
    
    def broadcast_burn_transaction_without_delay(self, burn_transaction):
        
        from Slimcoin.Network import Network as SlimcoinNetwork
        
        for node in SlimcoinNetwork.nodes.values():
            node.burn_transactions_memory_pool[burn_transaction.id] = burn_transaction
            
        # print(f"Node {self.id} has broadcasted transaction {transaction.id} to the network.\n")
        return burn_transaction
    
    
    def __str__(self):
        node_type = "Full"
        if not self.blockchain:
            node_type = "Lightweight"
        return f"Node(ID: {self.id}, Balance: {self.balance} SLM, Hashpower: {self.hashpower}, Type: {node_type})\n" 
    
    

def assign_miners():
    
    from Network import Network
    from itertools import combinations
    
    no_of_miners = random.choice(SlimcoinConfiguration.no_of_miners)
    SlimcoinConfiguration.miners = random.choice(list(combinations(Network.nodes.values(), no_of_miners)))
            
    for miner in SlimcoinConfiguration.miners:
        print(f"{miner.id} is a miner.")
    print("") 
    
    
def miners_burn_coins():
    
    for miner in SlimcoinConfiguration.miners:
        burn_value = random.randrange(10, 100)
        miner.burn_coins(burn_value)