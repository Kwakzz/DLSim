import random
import time
from Bitcoin.Block import Block as BitcoinBlock
from Configuration import BitcoinConfiguration
from Util import double_256_hash, get_chain_length
from Bitcoin.Nonce import Nonce
from Bitcoin.Block import genesis_block
from Node import Node as BaseNode


class Node (BaseNode):
    
    def __init__(
        self, 
        balance, 
        hashpower,
    ):
        super().__init__(
            balance,
        )
        self.blockchain = [genesis_block]
        self.hashpower = hashpower
        self.created_blocks = []


    def initiate_transaction(self):
        
        from Bitcoin.Transaction import Transaction as BitcoinTransaction
        from Network import Network
        
        if self.balance > 0:
            transaction_value = random.randrange(1, 5)
            other_nodes = random.sample(list(Network.nodes.values()), len(Network.nodes) - 1)  # Exclude sender
            recipient = random.choice(other_nodes)
            transaction = BitcoinTransaction(
                sender_id = self.id,
                recipient_id = recipient.id,
                value = transaction_value
            )
            
            transaction.set_hash()
            transaction.set_fee()
            
            # print(transaction)
            return transaction


    def create_block(self):
        block = BitcoinBlock()
        cumulative_transaction_size = 0
        
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
        
        block.parent_hash = self.blockchain[-1].hash
        
        block.set_merkle_root()
        block.set_hash()
        
        self.created_blocks.append(block)
        
        print(block)
        return block
    
    
    def scan_pow(self, block):
                
        sleep_time = 1/self.hashpower # time for single hash attempt
        time.sleep(sleep_time)
        
        nonce = Nonce.generate_nonce(self, block.nonce)

        combined_data = str(nonce) + block.hash
        
        block_hash = double_256_hash(combined_data)
        
        # print(f"Hash produced by node {self.id} is {block_hash}.")
        return block_hash, nonce
    
    
    def __str__(self):
        node_type = "Full"
        if not self.blockchain:
            node_type = "Lightweight"
        return f"Node(ID: {self.id}, Balance: {self.balance} BTC, Hashpower: {self.hashpower}, Type: {node_type})\n"
                
    
    
def assign_miners():
    
    from Bitcoin.Network import Network as BitcoinNetwork
    
    no_of_miners = random.choice(BitcoinConfiguration.no_of_miners)
    BitcoinConfiguration.miners = random.sample(list(BitcoinNetwork.nodes.values()), no_of_miners)
            
    for miner in BitcoinConfiguration.miners:
        print(f"{miner.id} is a miner.")
    print("")
        
        
def miners_create_blocks():
                
    for miner in BitcoinConfiguration.miners:
        print(f"{miner.id} is creating a block.")
        miner.create_block()