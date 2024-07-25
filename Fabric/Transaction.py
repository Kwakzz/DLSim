import random
from Configuration import FabricConfiguration
from datetime import datetime

from Util import sha256_hash

class Transaction:
    
    def __init__(self, asset, client_id, nonce, id=0):
        self.id = id
        self.client_id = client_id
        self.nonce = nonce
        self.asset = asset
        self.timestamp = datetime.now()
        self.size = random.choice(FabricConfiguration.transaction_size)
        self.confirmation_time = None
        
        
    def __str__(self):
        return f"""
        Transaction(
            id: {self.id},
            asset_id: {self.asset.id},
            client_id: {self.client_id},
            nonce: {self.nonce},
            timestamp: {self.timestamp},
            size: {self.size} bytes,
        )
        """
        
        
    def generate_transaction_id(self):
        id = self.nonce.to_bytes(4, byteorder='little') + bytes.fromhex(self.client_id)
        return (sha256_hash(id))
    
    
    def set_transaction_id(self):
        self.id = self.generate_transaction_id()

        
    


def peers_execute_transactions(endorsing_peers, proposals):
    
    proposals_with_majority_endorsement = []
    
    for proposal in proposals:
        
        for endorsing_peer in endorsing_peers:
            endorsing_peer.execute_transaction(proposal.transaction)
            
    # print("\nProposals with majority endorsement:")
    
    for proposal in proposals:
        transaction = proposal.transaction
        if transaction.has_majority_endorsement:
            proposals_with_majority_endorsement.append(proposal)
            # print(proposal)

                
    print(f"{len(proposals_with_majority_endorsement)} transactions have majority endorsement.")
                
    return proposals_with_majority_endorsement
            


def submit_transactions_to_leader(proposals):
    
    print("Clients are sending transactions with majority endorsement to the ordering service...")
    
    from Fabric.Network import Network as FabricNetwork
    
    for proposal in proposals:
        transaction = proposal.transaction
        client_id = proposal.client_id
        client = FabricNetwork.clients[client_id]
        client.submit_transaction_to_leader(transaction)
        
    
        
    