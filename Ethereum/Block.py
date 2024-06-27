from Block import Block as BaseBlock
from Configuration import EthereumConfiguration
from Ethereum.Slot import Slot
from Ethereum.Transaction import convert_eth_to_gwei

class Block (BaseBlock):
    
    def __init__(
        self, 
        hash=0, 
        parent_hash = None, 
        transactions = None,
        gas_used = 0,
        target_gas_usage = EthereumConfiguration.target_gas_usage,
        base_fee = EthereumConfiguration.current_base_fee,
        slot = Slot.current_slot_number,
    ):
        super().__init__(hash=0, parent_hash=None, transactions=None)
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
        return self.are_transactions_valid and self.parent_exists and self.is_slot_number_accurate
    
    
    # def __str__(self):
    #     return f"Block (\nID: {self.hash},\nParent: {self.parent_hash},\nTransactions: {list(self.transactions.keys())},\nSize: {self.size},\nNonce: {self.nonce}\n)\n"
    
    def __str__(self):
        return f"Block (\nID: {self.hash},\nParent: {self.parent_hash}, \nTimestamp: {self.timestamp}, \nTransactions: {list(self.transactions.keys())}, \nGas Used: {self.gas_used}, \nBase Fee: {convert_eth_to_gwei(self.base_fee)} gwei, \nSlot: {self.slot},"
        
        
    
        
        
    