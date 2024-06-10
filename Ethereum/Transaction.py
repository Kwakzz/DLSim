import random
from Block import Block
from Configuration import EthereumConfiguration, GeneralConfiguration
from Network import Network
from Transaction import Transaction as BaseTransaction

class Transaction (BaseTransaction):
    
    def __init__(self, recipient_id, sender_id, value, tip, gas_limit, id=0):
        super().__init__(recipient_id, sender_id, value, id=0)
        self.tip = tip
        self.gas_limit = gas_limit
    