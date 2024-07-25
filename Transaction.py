from datetime import datetime
from time import sleep
from Configuration import GeneralConfiguration, BitcoinConfiguration, EthereumConfiguration, SlimcoinConfiguration
from Network import Network 
import random
import sys
from Util import format_datetime, sha256_hash, transaction_delay


class Transaction:
    
    def __init__ (self, recipient_id, sender_id, value, id=0):
        self.id = id
        self.timestamp = datetime.now()
        self.recipient_id = recipient_id
        self.sender_id = sender_id
        self.value = value
        self.size = random.choice(GeneralConfiguration.transaction_size)
        self.confirmation_time = None
        
        
    def generate_hash(self):
        
        timestamp_int = int(self.timestamp.timestamp())
        
        header = (
            bytes.fromhex(self.recipient_id[::-1]) +  
            self.size.to_bytes(4, byteorder='little') +
            bytes.fromhex(self.sender_id[::-1]) +  
            timestamp_int.to_bytes(4, byteorder='little') +
            self.value.to_bytes(4, byteorder='little')
        )
        
        return sha256_hash(header)
    
    
    def set_hash(self):
        self.id = self.generate_hash()
    
        
    def transfer_funds(self, sender, recipient):
        sender.balance -= self.value
        recipient.balance += self.value
    
                
    def is_external_transfer(self):
        return self.sender_id == self.recipient_id
    
    
    def within_sender_balance(self):
        sender = Network.nodes[self.recipient_id]
        return self.value <= sender.balance
    
    
    def sender_exists(self):
        return Network.nodes[self.sender_id] != None
    
    
    def recipient_exists(self):
        return Network.nodes[self.recipient_id] != None
    
            
    def is_valid (self):
        return self.is_external_transfer and self.within_sender_balance and self.sender_exists and self.recipient_exists
            
        
        
def create_random_transactions(number_of_transactions):
    
    from Network import Network
        
        
    print("Nodes are conducting transactions...\n")
    for i in range(number_of_transactions):
        sender = random.choice(list(Network.nodes.values()))
        transaction = sender.initiate_transaction()
        # print(transaction)
        sender.broadcast_transaction_without_delay(transaction)
        
    transaction_delay()