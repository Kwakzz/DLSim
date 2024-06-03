import random
from Block import Block as BaseBlock
from Configuration import EthereumConfiguration, GeneralConfiguration, sha256_hash
from Network import Network
from Transaction import Transaction as BaseTransaction

class Transaction (BaseTransaction):
    
    def __init__(self, fee):
        super().__init__(
            fee=fee
        )
        self.fee = fee

    