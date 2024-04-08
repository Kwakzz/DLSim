from Network import Network
from Configuration import Configuration

class Block:
    
    def __init__(self, id,  miner_id, previous = None, timestamp = 0, size = 0, transactions = []):
        self.id = id
        self.previous = previous
        self.timestamp = timestamp
        self.size = size
        self.transactions = transactions
        self.miner_id = miner_id
        
        
    def are_transactions_valid(self):
        for transaction in self.transactions:
            if not transaction.is_sender_equal_to_recipient:
                return False
            
        return True
        
    
    