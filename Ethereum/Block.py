from Block import Block as BaseBlock
from Configuration import EthereumConfiguration
from Transaction import Transaction as BaseTransaction

class Block (BaseBlock):
    
    def __init__(self, id, balance):
        super().__init__(id=id, balance=balance)
        self.gas_limit = EthereumConfiguration.transaction_gas
        
        
    