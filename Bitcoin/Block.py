from Block import Block as BaseBlock
from Configuration import BitcoinConfiguration
from Util import convert_bytes_to_megabytes
from Bitcoin.Network import Network as BitcoinNetwork

class Block (BaseBlock):

    def __init__(
        self, 
        hash='0'*64,
        parent_hash=None,
        difficulty_target = hex(BitcoinNetwork.current_difficulty)
    ):
        super().__init__(hash='0'*64, parent_hash = None)
        self.difficulty_target = difficulty_target
        self.nonce = '0'*64
        
    
    def is_pow_valid(self):
        # print("Hash: " + str(len(str(int(self.hash, 16)))))
        # print("Difficulty: " + str(len(str(BitcoinNetwork.current_difficulty))))
        # print("Nonce:" + str(self.nonce))
        return int(self.hash, 16) < BitcoinNetwork.current_difficulty
    
    
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
            Difficulty Target: {self.difficulty_target} 
        )
        """ 
    
    

genesis_block = Block(
    hash='0'* 64,
    difficulty_target='0'*64
)