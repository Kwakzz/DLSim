from datetime import datetime
import random
from Block import Block as BaseBlock
from Configuration import GeneralConfiguration, BitcoinConfiguration
from Node import Node as BaseNode
from Bitcoin.Consensus import Consensus

class Block (BaseBlock):

    def __init__(
        self, 
        block_hash,
        difficulty_target = BitcoinConfiguration.difficulty_target, 
        nonce=0, 
        size=0, 
    ):
        super().__init__(difficulty_target, nonce, size)
        self.difficulty_target = BitcoinConfiguration.difficulty_target
        self.nonce = nonce
        self.size = size
        
 
genesis_block = Block(
    block_hash=0
)       
    
        