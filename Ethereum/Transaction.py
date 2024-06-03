import random
from Block import Block
from Configuration import EthereumConfiguration, GeneralConfiguration
from Network import Network
from Transaction import Transaction as BaseTransaction

class Transaction (BaseTransaction):
    
    def __init__(self):
        super().__init__(
            id=id, 
        )
        self.gas = random.randrange (EthereumConfiguration.transaction_gas_limit + 10) # the higher the transaction gas, the higher its chance of getting picked by a validator.
        self.tip = random.randrange(EthereumConfiguration.base_fee, EthereumConfiguration.base_fee + 100)  # a tip offered to a validator to increase a transaction's chance of being picked. also known as priority fee per gas
        
    def create_random_transaction(self):
        sender = random.choice(Network.nodes)
        recipient = random.choice(Network.nodes)
        amount_sent = random.randrange(1, sender.balance)
        tip = random.random(EthereumConfiguration.base_fee, EthereumConfiguration.base_fee+100)
        
        self.id = random.randrange(100000000000)
        self.timestamp = GeneralConfiguration.current_time
        self.sender_id = sender.id
        self.recipient_id = recipient.id
        self.amount_sent = amount_sent
        self.tip = tip
        self.fee = self.gas * (EthereumConfiguration.base_fee + self.tip)
        
        for node in Network.nodes:
            node.memory_pool.append(self)
         
    