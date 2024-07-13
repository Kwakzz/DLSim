import random
from Fabric.Asset import Asset
from Fabric.Proposal import Proposal        
from Configuration import FabricConfiguration


class Node:
    
    def __init__(self, id, blockchain = []):
        self.id = id
        self.blockchain = blockchain
        
        
    def __str__(self):
        return f"""
        Client {self.id}
        """
        
        
    def generate_create_transaction(self, asset_type):
        
        from Fabric.Transaction import CreateTransaction

        asset = Asset(type=asset_type, owner_id=self.id)
        transaction = CreateTransaction(owner=self, asset=asset)
        
        return transaction
        
    
    def generate_read_transaction(self, asset):
        
        from Fabric.Transaction import ReadTransaction

        transaction = ReadTransaction(asset=asset)
        
        return transaction
    
    
    def generate_delete_transaction(self, asset):
        
        from Fabric.Transaction import DeleteTransaction

        transaction = DeleteTransaction(asset=asset)
        
        return transaction
    
    
    def generate_transfer_transaction(self, asset):
        
        from Fabric.Transaction import TransferTransaction
        from Fabric.Network import Network as FabricNetwork
        
        other_nodes = random.sample(list(FabricNetwork.nodes.values()), len(FabricNetwork.nodes) - 1)  # Exclude sender
        recipient = random.choice(other_nodes)

        transaction = TransferTransaction(asset=asset, recipient=recipient)
        
        return transaction
        
    
        
    def generate_proposal(self, transaction):
                        
        proposal = Proposal(
            client_id=self.id,
            nonce=FabricConfiguration.proposal_counter,
            transaction=transaction
        )
        
        proposal.set_transaction_id()
        
        FabricConfiguration.proposal_counter += 1
        print(proposal)
        return proposal
        
    
    def submit_proposal(self, proposal):
        
        from Fabric.EndorsementPolicy import EndorsementPolicy
        
        endorsing_peers = EndorsementPolicy.select_endorsers()
        
        for endorsing_peer in endorsing_peers:
            endorsing_peer.transaction_memory_pool[proposal.transaction.id] = proposal
            
    
        
                   
            
            