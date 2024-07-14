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
        
    def __str__(self):
        return f"""
        Proposal (
           client: {self.client_id},
           transaction: {self.transaction.id}, 
           nonce: {self.nonce}
        )
        """
        
        
    def generate_transaction_id(self):
        id = self.nonce.to_bytes(4, byteorder='little') + bytes.fromhex(self.client_id)
        return (sha256_hash(id))
    
    
    def set_transaction_id(self):
        self.transaction.id = self.generate_transaction_id()
        
     
def generate_create_transaction_proposals():
    
    from Fabric.Network import Network as FabricNetwork
    
    proposals = []
    
    print("Clients are generating transaction proposals...")
    
    for i in range(FabricConfiguration.NO_OF_CLIENTS):
        node = random.choice(list(FabricNetwork.clients.values()))
        asset_type = random.choice(FabricConfiguration.ASSET_TYPES)
        transaction = node.generate_create_transaction(asset_type)
        proposal = node.generate_proposal(transaction)  
        proposals.append(proposal)
            
    print(f"{len(proposals)} proposals have been generated.")    
    return proposals 
    
        
def submit_proposals_to_peers(proposals, endorsing_peers):
    
    print("Clients are submitting their transaction proposals to endorsing peers...")
    
    from Fabric.Network import Network as FabricNetwork
    for proposal in proposals:
        client_id = proposal.client_id
        client = FabricNetwork.clients[client_id]
        client.submit_proposal_to_peers(proposal, endorsing_peers)
        
    
        
        
        
        
    
        