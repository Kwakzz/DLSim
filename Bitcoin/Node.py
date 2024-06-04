import random
from Bitcoin.Block import Block as BitcoinBlock, genesis_block
from Configuration import BitcoinConfiguration, set_bitcoin_transaction_fee, generate_block_hash, sha256_hash, generate_random_32_bit_number
from Node import Node as BaseNode


class Node (BaseNode):
    
    def __init__(
        self, 
        balance, 
        blockchain=[genesis_block], 
        transactions_memory_pool={}, 
        block_memory_pool={}
    ):
        super().__init__(
            balance,
            transactions_memory_pool={},
            block_memory_pool={}
        )
        self.blockchain = blockchain


    def initiate_transaction(self):
        
        from Bitcoin.Transaction import Transaction as BitcoinTransaction
        from Network import Network
        
        transaction_value = random.randrange(1, self.balance)
        other_nodes = random.sample(list(Network.nodes.values()), len(Network.nodes) - 1)  # Exclude sender
        recipient = random.choice(other_nodes)
        transaction = BitcoinTransaction(
            sender_id = self.id,
            recipient_id = recipient.id,
            value = transaction_value
        )
        transaction.id = sha256_hash(str(transaction))
        transaction.fee = set_bitcoin_transaction_fee(transaction.size)
        print(transaction)
        return transaction


    def create_block(self):
        block = BitcoinBlock()
        cumulative_transaction_size = 0
        
        for transaction in self.transactions_memory_pool.values():
            cumulative_transaction_size += transaction.size
            while cumulative_transaction_size < BitcoinConfiguration.block_size_limit:
                block.transactions[transaction.id] = transaction
        
        generate_block_hash(block)
                
        return block
    
    
    def scan_pow(self, block):
        nonce = generate_random_32_bit_number()
        block_hash = sha256_hash(str(block.id) + nonce)
        return block_hash
    
    
    def __str__(self):
        node_type = "Full"
        if not self.blockchain:
            node_type = "Lightweight"
        return f"Node(ID: {self.id}, Balance: {self.balance}, Type: {node_type})\n"
                
    