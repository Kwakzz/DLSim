from Block import Block as BaseBlock
from Configuration import BitcoinConfiguration

class Block (BaseBlock):

    def __init__(
        self, 
        hash=0,
        parent_hash=None,
        transaction_count = 0,
        transactions=None,
        difficulty_target = BitcoinConfiguration.difficulty_target, 
        nonce=0, 
        size=0, 
    ):
        super().__init__(hash=0, size=0, transaction_count=0, parent_hash = None, transactions = None)
        self.difficulty_target = BitcoinConfiguration.difficulty_target
        self.nonce = nonce
        
    
    def is_pow_valid(self):
        return self.hash.startswith("0"*self.difficulty_target)
    
    
    def parent_exists(self):
        
        from Network import Network
        
        for node in Network.nodes.values():
            for block in node.blockchain:
                if block.hash == self.parent_hash:
                    return True
                
        return False
    
    
    def is_valid(self):
        return self.is_pow_valid and self.are_transactions_valid and self.parent_exists
            
        
    # def __str__(self):
    #     return f"Block (\nID: {self.hash},\nParent: {self.parent_hash}, \nTimestamp: {self.timestamp}, \nTransactions: {list(self.transactions.keys())},\nTransaction Count: {self.transaction_count},\nSize: {self.size} MB,\nNonce: {self.nonce},\nDifficulty Target: {self.difficulty_target}\n)\n"
    
    
    def __str__(self):
        return f"Block (\nID: {self.hash},\nParent: {self.parent_hash}, \nTimestamp: {self.timestamp}, \nTransaction Count: {self.transaction_count},\nSize: {self.size} MB,\nNonce: {self.nonce},\nDifficulty Target: {self.difficulty_target}\n)\n" 
    
    

        