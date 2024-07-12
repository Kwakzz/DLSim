from Fabric.Chaincode import *

class Transaction:
    
    def __init__(self, asset, id=0, chaincode=None):
        self.id = id
        self.asset = asset
        self.chaincode = chaincode
        self.is_endorsed = False
        
        
        
class CreateTransaction(Transaction):
    
    def __init__(self, owner, asset, id=0, chaincode=create_asset_chaincode):
        super().__init__(asset=asset, id=id, chaincode=chaincode)
        self.owner = owner
        
        
        
class TransferTransaction(Transaction):
    
    def __init__(self, sender, recipient, asset, id=0, chaincode=transfer_asset_chaincode):
        super().__init__(asset=asset, id=id, chaincode=chaincode)
        self.sender = sender
        self.recipient = recipient
    
    
class ReadTransaction(Transaction):
    
    def __init__(self, owner, asset, id=0, chaincode=read_asset_chaincode):
        super().__init__(asset=asset, id=id, chaincode=chaincode)
        self.owner = owner
    
    
class DeleteTransaction(Transaction):
    
    def __init__(self, owner, asset, id=0, chaincode=delete_asset_chaincode):
        super().__init__(asset=asset, id=id, chaincode=chaincode)
        self.owner = owner
    
