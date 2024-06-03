from datetime import datetime
import random
from Bitcoin.Block import Block as BitcoinBlock, genesis_block
from Configuration import GeneralConfiguration, BitcoinConfiguration, set_bitcoin_transaction_fee, generate_block_hash, sha256_hash, generate_random_32_bit_number, is_pow_found
from Node import Node as BaseNode
from Bitcoin.Consensus import Consensus as PoW
from Bitcoin.Transaction import Transaction as BitcoinTransaction
import threading
import secrets

class Node (BaseNode):
    
    def __init__(
        self, 
        balance, 
        blockchain=[genesis_block], 
        transactions_memory_pool={}, 
        block_memory_pool={}
    ):
        super().__init__(
        )

    def initiate_transaction(self):
        from Bitcoin.Transaction import Transaction
        from Network import Network
        transaction_value = random.randrange(1, self.balance)
        recipient = random.choice(Network.nodes.values())
        transaction = Transaction(
            sender_id = self.id,
            recipient_id = recipient.id,
            value = transaction_value
        )
        transaction.fee = set_bitcoin_transaction_fee(transaction.size)
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
    
                
    