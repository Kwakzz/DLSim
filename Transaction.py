from Configuration import Configuration
from Network import Network 
import random

class Transaction:
    def __init__ (self, id=0, timestamp=0, recipient_id=0, sender_id=0, amount_sent=0, size = 0, fee = 0, is_confirmed=False):
        self.id = id
        self.timestamp = timestamp
        self.recipient_id = recipient_id
        self.sender_id = sender_id
        self.amount_sent = amount_sent
        self.size = size
        self.gas = Configuration.transaction_gas
        self.fee = fee
        self.is_confirmed = is_confirmed
                
    def is_sender_equal_to_recipient(self):
        return self.sender_id == self.recipient_id
    
    def is_amount_sent_greater_than_sender_balance(self):
        return self.amount_sent > self.sender.balance
                
    def within_block_limit (self):
        return self.gas_limit < Configuration.block_limit
    
    def is_valid (self):
        return not self.is_sender_equal_to_recipient and not self.is_amount_sent_greater_than_sender_balance
    
    def create_random_transaction(self):
        sender = random.choice(Network.nodes)
        recipient = random.choice(Network.nodes)
        amount_sent = random.randrange(1, sender.balance + 100)
        
        self.id = random.randrange(100000000000)
        self.timestamp = Configuration.current_time
        self.sender_id = sender.id
        self.recipient_id = recipient.id
        self.amount_sent = amount_sent
        
        for node in Network.nodes:
            node.memory_pool.append(self)

        
