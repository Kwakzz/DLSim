from Block import Block as BaseBlock
from Configuration import EthereumConfiguration
from Transaction import Transaction as BaseTransaction
import random

class Block (BaseBlock):
    
    def __init__(self, hash, balance):
        super().__init__(block_hash=hash, balance=balance)
        self.gas_limit = EthereumConfiguration.transaction_gas
        self.base_fee = random.randrange(0.001, 0.002) # the minimum price per gas for a transaction to be eligible for selection
        
    
        
        
    