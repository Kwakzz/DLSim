import random
from Bitcoin.Block import Block as BitcoinBlock, genesis_block
from Configuration import BitcoinConfiguration
from Util import sha256_hash, generate_nonce
from Block import generate_block_hash
from Node import Node as BaseNode


class Node (BaseNode):
    
    def __init__(
        self, 
        balance, 
        blockchain=[genesis_block], 
        transactions_memory_pool=None, 
        block_memory_pool=None,
        created_blocks=None,
        hashpower = 0
    ):
        super().__init__(
            balance,
            transactions_memory_pool=None,
            block_memory_pool=None,
            created_blocks=None
        )
        self.blockchain = blockchain
        self.hashpower = hashpower


    def initiate_transaction(self):
        
        from Bitcoin.Transaction import Transaction as BitcoinTransaction
        from Network import Network
        
        if self.balance != 0:
            transaction_value = random.randrange(0, self.balance//2.5)
            other_nodes = random.sample(list(Network.nodes.values()), len(Network.nodes) - 1)  # Exclude sender
            recipient = random.choice(other_nodes)
            transaction = BitcoinTransaction(
                sender_id = self.id,
                recipient_id = recipient.id,
                value = transaction_value
            )
            transaction.id = sha256_hash(str(transaction))
            transaction.set_fee()
            
            print(transaction)
            return transaction


    def create_block(self):
        block = BitcoinBlock()
        cumulative_transaction_size = 0
        
        for transaction in self.transactions_memory_pool.values():
            cumulative_transaction_size += transaction.size
            if cumulative_transaction_size < BitcoinConfiguration.block_size_limit and transaction.is_valid():
                block.transactions[transaction.id] = transaction
            else:
                break
        
        generate_block_hash(block)
        block.size=cumulative_transaction_size
        
        block.parent_hash = self.blockchain[-1].hash
        
        self.created_blocks.append(block)
        
        print(block)
        return block
    
    
    def scan_pow(self, block):
        nonce = generate_nonce()
        block_hash = sha256_hash(str(block.hash) + nonce)
        print(f"Hash produced by node {self.id} is {block_hash}.")
        return block_hash
    
    
    def __str__(self):
        node_type = "Full"
        if not self.blockchain:
            node_type = "Lightweight"
        return f"Node(ID: {self.id}, Balance: {self.balance}, Type: {node_type})\n"
                
    
    
def assign_miners():
    
    from Network import Network
    from itertools import combinations
    
    
    BitcoinConfiguration.miners = random.choice(list(combinations(Network.nodes.values(), 3)))
            
    for miner in BitcoinConfiguration.miners:
        print(f"{miner.id} is a miner\n")
        
        
def miners_create_blocks():
    
    from Network import Network
    from itertools import combinations
    
    BitcoinConfiguration.miners = random.choice(list(combinations(Network.nodes.values(), 3)))
            
    for miner in BitcoinConfiguration.miners:
        print(f"{miner.id} is creating a block.")
        miner.create_block()