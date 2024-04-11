from Block import Block as BaseBlock
from Configuration import Configuration
from Transaction import Transaction as BaseTransaction

class Block (BaseBlock):
    
    def __init__(self, id, balance):
        super().__init__(id=id, balance=balance)
        self.gas_limit = Configuration.transaction_gas
        
        
    