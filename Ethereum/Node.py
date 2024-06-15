import random
from Block import Block
from Configuration import GeneralConfiguration, EthereumConfiguration
from Block import generate_block_hash, genesis_block
from Node import Node as BaseNode

class Node (BaseNode):
    
    def __init__(
        self, 
        balance, 
        blockchain=[genesis_block], 
        transactions_memory_pool=None, 
        block_memory_pool=None,
        created_blocks=None,
    ):
        super().__init__(
            balance,
            transactions_memory_pool=None,
            block_memory_pool=None,
            created_blocks=None,
        )
        self.blockchain = blockchain
        
        
    def initiate_transaction(self):
        
        from Ethereum.Transaction import Transaction as EthereumTransaction
        from Util import sha256_hash
        from Network import Network
        
        if self.balance > 0:
            transaction_value = random.randrange(0, self.balance//2.5)
            other_nodes = random.sample(list(Network.nodes.values()), len(Network.nodes) - 1)  # Exclude sender
            recipient = random.choice(other_nodes)
            transaction = EthereumTransaction(
                sender_id = self.id,
                recipient_id = recipient.id,
                value = transaction_value
            )
            
            transaction.id = sha256_hash(str(transaction))
            
            print(transaction)
            return transaction
        
        
    def __str__(self):
        return f"Node(ID: {self.id}, Balance: {self.balance})\n"
    
    
        