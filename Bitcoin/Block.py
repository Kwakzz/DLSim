from Block import Block as BaseBlock
from Configuration import BitcoinConfiguration

class Block (BaseBlock):

    def __init__(
        self, 
        hash,
        difficulty_target = BitcoinConfiguration.difficulty_target, 
        nonce=0, 
        size=0, 
    ):
        super().__init__(difficulty_target, nonce, size)
        self.difficulty_target = BitcoinConfiguration.difficulty_target
        self.nonce = nonce
        self.size = size
        
 
genesis_block = Block(
    hash=0
)       
    
        