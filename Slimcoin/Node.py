import random
from Bitcoin.Node import Node as BitcoinNode
from Configuration import BitcoinConfiguration, SlimcoinConfiguration
from Slimcoin.BurnTransaction import BurnTransaction
from Slimcoin.Block import Block as SlimcoinBlock
from Util import get_chain_length, transaction_propagation_delay

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
        
    
    def initiate_transaction(self):
        
        from Slimcoin.Transaction import Transaction as SlimcoinTransaction
        from Network import Network
        
        if self.balance > 0:
            transaction_value = random.randrange(1, 5)
            other_nodes = random.sample(list(Network.nodes.values()), len(Network.nodes) - 1)  # Exclude sender
            recipient = random.choice(other_nodes)
            transaction = SlimcoinTransaction(
                sender_id = self.id,
                recipient_id = recipient.id,
                value = transaction_value
            )
            
            transaction.set_hash()
            transaction.set_fee()
            
            # print(transaction)
            return transaction
        
    
    def burn_coins(self, value):
        
        from Slimcoin.Consensus import Consensus as PoB

        burn_transaction = BurnTransaction(
            value = value,
            sender_id = self.id
        )

        burn_transaction.set_hash()
        burn_transaction.set_burn_hash()
        self.balance -= value
        
        self.broadcast_burn_transaction(burn_transaction)
        transaction_propagation_delay()
        
        print(burn_transaction)
        # print(f"Burn Hash: {int(burn_transaction.get_burn_hash(), 16)}")
        # print(f"Burn Hash Target: {int(PoB.burn_hash_target, 16)}")
        return burn_transaction
    
    
    def broadcast_burn_transaction(self, burn_transaction):
        
        from Slimcoin.Network import Network as SlimcoinNetwork
        
        for node in SlimcoinNetwork.nodes.values():
            node.burn_transactions_memory_pool[burn_transaction.id] = burn_transaction
        
        transaction_propagation_delay()
            
        # print(f"Node {self.id} has broadcasted burn transaction {transaction.id} to the network.\n")
        return burn_transaction
    
    
    def create_pow_block(self):
        return super().create_block()
    
    
    def create_pob_block(self, burn_transaction):
        
        print(f"{self.id} is creating a PoB block.")
        
        block = SlimcoinBlock()
        
        block.transactions[burn_transaction.id] = burn_transaction
        cumulative_transaction_size = burn_transaction.size
        
        transactions_memory_pool_copy = list(self.transactions_memory_pool.values())
        for transaction in transactions_memory_pool_copy:
            if cumulative_transaction_size + transaction.size > BitcoinConfiguration.BLOCK_SIZE_LIMIT:
                break
            if transaction.is_valid():
                block.transactions[transaction.id] = transaction
                cumulative_transaction_size += transaction.size
        
        block.size=cumulative_transaction_size
        block.transaction_count = len(block.transactions)
        block.height = get_chain_length()
        block.burn_hash = burn_transaction.burn_hash
        
        block.parent_hash = self.blockchain[-1].hash
        
        block.set_merkle_root()
        block.set_hash()
                
        print(block)
        return block
    
    
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
        
        
def miners_create_pow_blocks():
                
    for miner in SlimcoinConfiguration.miners:
        print(f"{miner.id} is creating a  PoW block.")
        miner.create_pow_block()