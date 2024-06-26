from datetime import datetime

class Block:
    
    def __init__(self, hash=0, parent_hash = None, transactions = None):
        self.hash = hash
        self.parent_hash = parent_hash
        self.timestamp = datetime.now()
        self.transactions = transactions if transactions is not None else {}
        
        
    def are_transactions_valid(self):
        for transaction in self.transactions.values():
            if not transaction.is_valid:
                return False      
        return True
    
    
    def add_to_chain(self):
        
        from Network import Network
        
        for node in Network.nodes.values():
            if self not in node.blockchain:
                node.blockchain.append(self)
        
        print(f"{self.hash} has been added to the chain.\n")
        
        
    def finalize_transactions(self, creator):
        for transaction in self.transactions.values():
            transaction.finalize(creator)
        print(f"Block {self.hash} transactions have been finalized.")
        

    
    def __eq__(self, other):
        if not isinstance (other, Block):
            return False
        return self.hash == other.hash
        
        
        
def generate_block_hash(block):
    
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
    
    
    
genesis_block = Block(
    hash=0
) 