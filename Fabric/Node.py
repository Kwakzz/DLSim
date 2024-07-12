import random
from Fabric.Asset import Asset
from Fabric.Proposal import Proposal


class Node:
    
    def __init__(self, id, blockchain = []):
        self.id = id,
        self.blockchain = blockchain
        
        
    def generate_create_transaction(self, asset_type):
        
        from Fabric.Transaction import CreateTransaction

        asset = Asset(type=asset_type, owner_id=self.id)
        transaction = CreateTransaction(owner=self, asset=asset)
        
        return transaction
        
    
    def generate_read_transaction(asset):
        
        from Fabric.Transaction import ReadTransaction

        transaction = ReadTransaction(asset=asset)
        
        return transaction
    
    
    def generate_delete_transaction(asset):
        
        from Fabric.Transaction import DeleteTransaction

        transaction = DeleteTransaction(asset=asset)
        
        return transaction
    
    
    def generate_transfer_transaction(asset):
        
        from Fabric.Transaction import TransferTransaction

        transaction = TransferTransaction(asset=asset)
        
        return transaction
    
    
        
    def generate_proposal(self, transaction):
        
        from Configuration import FabricConfiguration
        
        chaincode = transaction.chaincode
        chaincode_id = chaincode.id
        
        proposal = Proposal(
            client_id=self.id,
            chaincode_id=chaincode_id,
            nonce=FabricConfiguration.proposal_counter,
            transaction=transaction
        )
        
        FabricConfiguration.proposal_counter += 1
        
        return proposal
        
    
    def submit_proposal(self, proposal):
        pass
    
    