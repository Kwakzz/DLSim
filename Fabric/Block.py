from datetime import datetime
from Configuration import GeneralConfiguration
from Util import double_256_hash, sha256_hash


class Block:
    
    def __init__(self, sequence_number, hash=0, parent_hash=None, transactions=None, merkle_root = '0'*64):
        self.hash = hash
        self.parent_hash = parent_hash
        self.timestamp = datetime.now()
        self.merkle_root = merkle_root
        self.transactions = transactions if transactions is not None else {}
        self.transaction_count = 0
        self.sequence_number = sequence_number
        self.height = 0
        self.size = 0
        
    
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
        
        
    def __str__(self):
        size = round(self.size, 2)
        return f"""
        Block (
            Hash: {self.hash},
            Parent: {self.parent_hash},
            Merkle Root: {self.merkle_root},
            Timestamp: {self.timestamp},
            Block Height: {self.height},
            Transaction Count: {self.transaction_count},
            Sequence Number: {self.sequence_number}
        )"""
        
 
genesis_block = Block(
    hash='0' * 64,
    sequence_number=0
)       
        
    