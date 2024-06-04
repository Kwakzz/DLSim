from Block import Block as BaseBlock
from Configuration import BitcoinConfiguration

class Block (BaseBlock):

    def __init__(
        self, 
        hash=0,
        parent_hash=None,
        transactions={},
        difficulty_target = BitcoinConfiguration.difficulty_target, 
        nonce=0, 
        size=0, 
    ):
        super().__init__(hash=0, parent_hash = None, transactions = {})
        self.difficulty_target = BitcoinConfiguration.difficulty_target
        self.nonce = nonce
        self.size = size
        
    def __str__(self):
        return f"Block (\nID: {self.hash},\nParent: {self.parent_hash},\nTransactions: {self.transactions.keys()},\nSize: {self.size},\nNonce: {self.nonce},\nDifficulty Target: {self.difficulty_target}\n)\n"
        
 
genesis_block = Block(
    hash=0
)       
    
    

        