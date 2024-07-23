from Configuration import SlimcoinConfiguration
from Bitcoin.Block import Block as BitcoinBlock

class Node (BitcoinBlock):
    
    def __init__(
        self, 
        hash='0'*64,
    ):
        super().__init__(
            hash='0'*64, parent_hash = None
        )
        self.burn_hash_target = SlimcoinConfiguration.current_burn_hash_target,
        self.burn_hash = None
        
    
    