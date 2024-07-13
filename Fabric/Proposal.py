import random
from Configuration import FabricConfiguration
from Util import sha256_hash

class Proposal:
    
    def __init__(self, client_id, nonce, transaction):
        self.client_id = client_id
        self.transaction = transaction
        self.chaincode_id = transaction.chaincode.id
        self.nonce = nonce
        self.endorsements = {}
        
        
    def generate_transaction_id(self):
        id = self.nonce.to_bytes(4, byteorder='little') + bytes.fromhex(self.client_id)
        return (sha256_hash(id))
    
    
    def set_transaction_id(self):
        self.transaction.id = self.generate_transaction_id()
        
     
def generate_create_transaction_proposals():
    
    from Fabric.Network import Network as FabricNetwork
    
    proposals = []
    
    for i in range(FabricConfiguration.PROPOSAL_COUNT_PER_ROUND):
        
        node = random.choice(FabricNetwork.clients)
                
        asset_type = random.choice(FabricConfiguration.ASSET_TYPES)
        transaction = node.generate_create_transaction(asset_type)
        proposal = node.generate_proposal(transaction)  
        proposals.append(proposal)
        
    return proposals 
    
        
def submit_proposals(proposals):
    
    from Fabric.Network import Network as FabricNetwork
    for proposal in proposals:
        client_id = proposal.client_id
        client = FabricNetwork.clients[client_id]
        client.submit_proposal(proposal)
        
        
        
        
    
        