from datetime import datetime

class Block:
    
    def __init__(self, hash=0, parent_hash = None, transactions = {}):
        self.hash = hash
        self.parent_hash = parent_hash
        self.timestamp = datetime.now()
        self.transactions = transactions
        
        
    def are_transactions_valid(self):
        for transaction in self.transactions.values():
            if not transaction.is_valid:
                return False      
        return True
        
    
    def __is_eq__(self, other):
        if not isinstance (other, Block):
            return False
        return self.id == other.id 
        
        
        
def generate_block_hash(block):
    
    import string
    from Util import sha256_hash
    
    number_of_transactions = len(block.transactions)
    transaction_hashes = []
    paired_transaction_hashes = []
    
    for transaction in block.transactions.values():
        transaction_hashes.append(transaction.id)
        
    if (number_of_transactions % 2 == 1):
        transaction_hashes.append(transaction_hashes[-1]) # duplicate final hash if list is odd-numbered
        
    for i in range (0, len(transaction_hashes)-1, 2):
        paired_transaction_hash = sha256_hash(transaction_hashes[i] + transaction_hashes[i+1])
        paired_transaction_hashes.append(paired_transaction_hash)
        
    separator = ""
    block.hash = separator.join([str(transaction_hash) for transaction_hash in paired_transaction_hashes])
    return block.hash
    
    