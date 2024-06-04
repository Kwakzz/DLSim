from datetime import datetime
from Configuration import GeneralConfiguration, sha256_hash
from Network import Network 
import random
import sys


class Transaction:
    
    def __init__ (self, recipient_id, sender_id, value, id=0):
        self.id = id
        self.timestamp = datetime.now()
        self.recipient_id = recipient_id
        self.sender_id = sender_id
        self.value = value
        self.size = sys.getsizeof(self)
    
                
    def is_external_transfer(self):
        return self.sender_id == self.recipient_id
    
    
    def within_sender_balance(self):
        sender = Network.nodes[self.recipient_id]
        return self.value > sender.balance
    
    
    def sender_exists(self):
        return Network.nodes[self.sender_id] != None
    
    
    def recipient_exists(self):
        return Network.nodes[self.recipient_id] != None
    
            
    def is_valid (self):
        return self.is_external_transfer and self.within_sender_balance and self.sender_exists and self.recipient_exists
    
    
            

        
