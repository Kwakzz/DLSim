import random
from Ethereum.Block import genesis_block
from Configuration import EthereumConfiguration
from Ethereum.Block import Block as EthereumBlock
from Ethereum.DepositContract import DepositContract
from Node import Node as BaseNode
from Util import get_chain_length

class Node (BaseNode):
    
    def __init__(
        self, 
        balance, 
    ):
        super().__init__(
            balance
        )
        self.blockchain = [genesis_block]
        
        
    def initiate_transaction(self):
        
        from Ethereum.Transaction import Transaction as EthereumTransaction
        from Util import sha256_hash
        from Network import Network
        
        transaction_value = 0
        
        if self.balance > 0:
            transaction_value = random.randrange(1, 5)
                         
            other_nodes = random.sample(list(Network.nodes.values()), len(Network.nodes) - 1)  # Exclude sender
            recipient = random.choice(other_nodes)
            transaction = EthereumTransaction(
                sender_id = self.id,
                recipient_id = recipient.id,
                value = transaction_value
            )
            
            transaction.set_hash()
            
            # print(transaction)
            return transaction
        
        
    def stake(self, amount):
        DepositContract.deposits[self.id] += amount
        print(f"{self.id} has staked {amount} ETH into the deposit contract.")
        return amount
        
        
    def create_block(self):
        block = EthereumBlock()
        cumulative_transaction_gas = 0
        cumulative_transaction_size = 0
        
        transactions_memory_pool_copy = list(self.transactions_memory_pool.values())
        for transaction in transactions_memory_pool_copy:
            if cumulative_transaction_gas + transaction.gas_used > EthereumConfiguration.BLOCK_GAS_LIMIT:
                break
            if transaction.is_valid():
                block.transactions[transaction.id] = transaction
                cumulative_transaction_gas += transaction.gas_used
                cumulative_transaction_size = transaction.size
        
        block.gas_used=cumulative_transaction_gas
        block.size = cumulative_transaction_size
        block.height = get_chain_length()
        
        block.transaction_count = len(block.transactions)
        
        block.parent_hash = self.blockchain[-1].hash
        
        block.set_merkle_root()
        block.set_hash()
                
        print(f"{self.id} has created block {block.hash}")
        print(block)
        return block
    
    
    def generate_secret_value(self):
        import secrets  
        return secrets.token_bytes(32)
            
        
    def __str__(self):
        return f"Node(ID: {self.id}, Balance: {self.balance} ETH)\n"