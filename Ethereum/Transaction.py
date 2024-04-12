import random
from Block import Block
from Configuration import EthereumConfiguration
from Transaction import Transaction as BaseTransaction

class Transaction (BaseTransaction):
    
    def __init__(self):
        super().__init__(id=id)
        self.gas = random.randrange (EthereumConfiguration.transaction_gas_limit + 10)
        
        
    