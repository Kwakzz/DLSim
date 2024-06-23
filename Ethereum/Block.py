from Block import Block as BaseBlock
from Configuration import EthereumConfiguration
from Transaction import Transaction as BaseTransaction
import random

class Block (BaseBlock):
    
    def __init__(self, target_gas_usage, base_fee, slot, hash=0, parent_hash = None, transactions = None):
        super().__init__(hash=0, parent_hash=None, transactions=None)
        gas_used = 0
        target_gas_usage = EthereumConfiguration.target_gas_usage
        base_fee = EthereumConfiguration.current_base_fee
        slot = EthereumConfiguration.c
        
        
    def is_valid(self):
        return self.are_transactions_valid and self.parent_exists
    
    
    def __str__(self):
        return f"Block (\nID: {self.hash},\nParent: {self.parent_hash},\nTransactions: {list(self.transactions.keys())},\nSize: {self.size},\nNonce: {self.nonce}\n)\n"
        
        
    
        
        
    