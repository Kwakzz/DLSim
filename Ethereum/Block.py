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
        transaction_count = 0,
        transactions = None,
        gas_used = 0,
        target_gas_usage = EthereumConfiguration.target_gas_usage,
        base_fee = EthereumConfiguration.current_base_fee,
        slot = Slot.current_slot_number,
        size = 0,
        merkle_root = '0'*64,
    ):
        super().__init__(hash='0'*64, size=0, transaction_count=0, parent_hash=None, transactions=None, merkle_root='0'*64,)
        self.gas_used = 0
        self.target_gas_usage = target_gas_usage
        self.base_fee = base_fee
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
        return self.are_transactions_valid and self.parent_exists and self.is_slot_number_accurat
    
    
    def __str__(self):
        size_in_bytes = round(self.size, 2)
        return f"""
            Block (\n
                Hash: {self.hash}, \n
                Parent: {self.parent_hash}, \n
                Timestamp: {self.timestamp}, \n
                Transaction Count: {self.transaction_count}, \n
                Gas Used: {self.gas_used} units, \n
                Size: {size_in_bytes} bytes, \n
                Base Fee Used: {convert_eth_to_gwei(self.base_fee)} gwei, \n
                Slot: {self.slot} \n
            )
            """
        
        
    
genesis_block = Block(
    hash='0' * 64
)         
        
    