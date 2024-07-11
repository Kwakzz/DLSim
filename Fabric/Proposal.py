from Util import sha256_hash

class Proposal:
    
    def __init__(self, client_id, smart_contract_id, nonce, transaction):
        self.client_id = client_id
        self.transaction = transaction
        self.smart_contract_id = smart_contract_id
        self.nonce = nonce
        self.endorsements = {}
        
        
    def generate_transaction_id(self):
        id = self.nonce.to_bytes(4, byteorder='little') + bytes.fromhex(self.client_id)
        return (sha256_hash(id))
    
    
    def set_transaction_id(self):
        self.transaction.id = self.generate_transaction_id()
        
        
    
        
        
    
        