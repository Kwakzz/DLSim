from datetime import datetime

class Block:
    
    def __init__(self, block_hash, parent_id = None, transactions = {}):
        self.hash = block_hash
        self.parent_id = parent_id
        self.timestamp = datetime.now()
        self.transactions = transactions
        
        
    def are_transactions_valid(self):
        for transaction in self.transactions.values():
            if not transaction.is_valid:
                return False      
        return True
        
    
    