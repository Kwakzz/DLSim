from Configuration import SlimcoinConfiguration
from Bitcoin.Block import Block as BitcoinBlock
from Slimcoin.PoB import PoB

class Block (BitcoinBlock):
    
    def __init__(
        self, 
        hash='0'*64,
    ):
        super().__init__(
            hash='0'*64, parent_hash = None
        )
        self.burn_hash_target = PoB.burn_hash_target_in_hex
        self.burn_hash = None
    
            
            
    def is_valid(self):
        return self.are_transactions_valid and self.parent_exists
        
    
    def __str__(self):
        size_in_bytes = round(self.size, 2)
        return f"""
        Block (
            Hash: {self.hash}, 
            Parent: {self.parent_hash}, 
            Timestamp: {self.timestamp}, 
            Block Height: {self.height},
            Transaction Count: {self.transaction_count}, 
            Nonce: {self.nonce}, 
            Size: {size_in_bytes} bytes, 
            Burn Hash: {self.burn_hash},
            Burn Hash Target: {self.burn_hash_target},
        )
        """ 
    