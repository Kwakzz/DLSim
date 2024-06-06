import random
from Block import Block
from Configuration import EthereumConfiguration, GeneralConfiguration
from Network import Network
from Transaction import Transaction as BaseTransaction

class Transaction (BaseTransaction):
    
    def __init__(self):
        super().__init__()
    