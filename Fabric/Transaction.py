from Configuration import GeneralConfiguration
from datetime import datetime
from Fabric.Chaincode import *

class Transaction:
    
    def __init__(self, asset, id=0, chaincode=None):
        self.id = id
        self.asset = asset
        self.timestamp = datetime.now()
        self.chaincode = chaincode
        self.endorsements = {}
        self.size = random.choice(GeneralConfiguration.transaction_size)
        self.is_commited = False
        self.confirmation_time = None
        
        
    def __str__(self):
        return f"""
        Transaction(
            id: {self.id},
            asset_id: {self.asset.id},
            chaincode_id: {self.chaincode.id},
            size: {self.size} bytes,
            no_of_endorsement: {len(self.endorsements)}
        )
        """
        
        
    def has_majority_endorsement(self):
        from Fabric.Network import Network as FabricNetwork
        
        no_of_endorsements = len(self.endorsements)
        count_of_half_of_peers = len(FabricNetwork.peers) // 2
        
        return no_of_endorsements > count_of_half_of_peers

        
        
class CreateTransaction(Transaction):
    
    def __init__(self, owner, asset, id=0, chaincode=create_asset_chaincode):
        super().__init__(asset=asset, id=id, chaincode=chaincode)
        self.owner = owner
         
        
class TransferTransaction(Transaction):
    
    def __init__(self, recipient, asset, id=0, chaincode=transfer_asset_chaincode):
        super().__init__(asset=asset, id=id, chaincode=chaincode)
        self.recipient = recipient
    
    
class ReadTransaction(Transaction):
    
    def __init__(self, asset, id=0, chaincode=read_asset_chaincode):
        super().__init__(asset=asset, id=id, chaincode=chaincode)
    
    
class DeleteTransaction(Transaction):
    
    def __init__(self, asset, id=0, chaincode=delete_asset_chaincode):
        super().__init__(asset=asset, id=id, chaincode=chaincode)
    


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
        
    