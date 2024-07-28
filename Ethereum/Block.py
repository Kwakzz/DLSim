from Block import Block as BaseBlock
from Configuration import EthereumConfiguration
from Ethereum.Slot import Slot
from Ethereum.Transaction import convert_eth_to_gwei
from Util import convert_bytes_to_megabytes

class Block (BaseBlock):
    
    def __init__(
        self, 
        hash='0'*64, 
        parent_hash = None, 
        slot = Slot.current_slot_number
    ):
        super().__init__(hash='0'*64, parent_hash=None)
        self.gas_used = 0
        self.target_gas_usage = EthereumConfiguration.target_gas_usage
        self.base_fee = EthereumConfiguration.current_base_fee
        self.slot = slot
        
        
    def is_slot_number_accurate(self):
        return self.slot == Slot.current_slot_number
    
    
    def parent_exists(self):
        
        from Ethereum.Network import Network as EthereumNetwork
        
        for node in EthereumNetwork.nodes.values():
            for block in node.blockchain:
                if block.hash == self.parent_hash:
                    return True
        
        
    def is_valid(self):
        return self.are_transactions_valid and self.parent_exists and self.is_slot_number_accurate
    
    
    def __str__(self):
        size_in_bytes = round(self.size, 2)
        return f"""
        Block (\n
            Hash: {self.hash}, 
            Parent: {self.parent_hash}, 
            Timestamp: {self.timestamp},
            Block Height: {self.height},
            Transaction Count: {self.transaction_count}, 
            Gas Used: {self.gas_used} units, 
            Size: {size_in_bytes} bytes, 
            Base Fee Used: {convert_eth_to_gwei(self.base_fee)} gwei, 
            Slot: {self.slot} 
        )
        """
        
        
    
genesis_block = Block(
    hash='0' * 64
)         
        
    