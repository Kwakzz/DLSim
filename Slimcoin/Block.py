from Configuration import SlimcoinConfiguration
from Bitcoin.Block import Block as BitcoinBlock
from Slimcoin.Consensus import Consensus as PoB

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
        
        
    def is_pob_block(self):
        if self.burn_hash:
            return True
        return False
    
    
    def finalize_transactions(self, block_creator):
        for transaction in self.transactions.values():
            if transaction.is_burn_transaction():
                transaction.finalize()
            else:    
                transaction.finalize(block_creator)
        print(f"Block {self.hash} transactions have been finalized.")

    
    def is_burn_hash_accurate(self):
        
        for transaction in self.transactions.values():
            if transaction.is_burn_transaction:
                return transaction.burn_hash == self.burn_hash
            
            
    def is_valid(self):
        return self.are_transactions_valid() and self.parent_exists() and self.is_burn_hash_accurate()
        
    
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
    