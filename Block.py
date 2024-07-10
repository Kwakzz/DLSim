from datetime import datetime
from Configuration import GeneralConfiguration
from Util import convert_bytes_to_megabytes, double_256_hash, sha256_hash

class Block:
    
    def __init__(self, hash='0'*64, size=0, transaction_count=0, parent_hash = None, transactions = None, merkle_root = '0'*64):
        self.hash = hash
        self.parent_hash = parent_hash
        self.timestamp = datetime.now()
        self.merkle_root = merkle_root
        self.transactions = transactions if transactions is not None else {}
        self.transaction_count = transaction_count
        self.size = size
        
        
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
    
    
    def generate_merkle_root(self):
        number_of_transactions = len(self.transactions)
        transaction_hashes = []

        for transaction in self.transactions.values():
            transaction_hashes.append(bytes.fromhex(transaction.id))
            
        if number_of_transactions % 2 == 1:
            transaction_hashes.append(transaction_hashes[-1])  # duplicate final hash if list is odd-numbered
        
        while len(transaction_hashes) > 1:
            new_hashes = []
            
            for i in range(0, len(transaction_hashes), 2):
                combined = transaction_hashes[i] + transaction_hashes[i + 1]
                new_hash = bytes.fromhex(double_256_hash(combined))
                new_hashes.append(new_hash)
            
            if len(new_hashes) % 2 == 1:
                new_hashes.append(new_hashes[-1])
                                
            transaction_hashes = new_hashes
            
            if len(transaction_hashes) == 2:
                combined = transaction_hashes[0] + transaction_hashes[1]
                new_hash = bytes.fromhex(double_256_hash(combined))
                transaction_hashes = [new_hash]
                
            # print(len(transaction_hashes))            

        merkle_root = transaction_hashes[0]  
        return merkle_root  
    
    
    def set_merkle_root(self):
        self.merkle_root = self.generate_merkle_root()
    
    
    def generate_hash(self):
        
        timestamp_int = int(self.timestamp.timestamp())
        nonce_int = 0
        
        header = ""
        
        if GeneralConfiguration.selected_platform == "Bitcoin":
            
            nonce_int = int(self.nonce)
            
            header = (
                bytes.fromhex(self.parent_hash)[::-1] +  
                self.merkle_root[::-1] +  
                timestamp_int.to_bytes(4, byteorder='little') +
                nonce_int.to_bytes(4, byteorder='little')
            )
            
        else:
            header = (
                bytes.fromhex(self.parent_hash)[::-1] +  
                self.merkle_root[::-1] +  
                timestamp_int.to_bytes(4, byteorder='little')
            )
            
        return sha256_hash(header)
        
        
    def set_hash(self):
        self.hash = self.generate_hash()
        
        
    def __eq__(self, other):
        if not isinstance (other, Block):
            return False
        return self.hash == other.hash
    
    
    def __str__(self):
        size_in_mb = convert_bytes_to_megabytes(self.size)
        return f"Block (\Hash: {self.hash},\nParent: {self.parent_hash}, \nTimestamp: {self.timestamp}, \nTransactions: {list(self.transactions.keys())},\nTransaction Count: {self.transaction_count},\nSize: {size_in_mb} MB\n)\n"
            