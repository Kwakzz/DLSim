from Block import Block as BaseBlock
from Configuration import EthereumConfiguration
from Transaction import Transaction as BaseTransaction
import random

class Block (BaseBlock):
    
    def __init__(self, target_gas_usage, base_fee, hash=0, parent_hash = None, transactions = None):
        super().__init__(hash=0, parent_hash=None, transactions=None)
        gas_used = 0
        target_gas_usage = 0
        base_fee = EthereumConfiguration.current_base_fee
        
        
        
    
        
        
    