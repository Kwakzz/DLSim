import random
from Fabric.Asset import Asset
from Util import generate_id
from Fabric.EndorsementPolicy import EndorsementPolicy


class Chaincode:
    
    def __init__(self):
        self.id = generate_id
        self.endorsers = {}
        self.contract = None
        self.events = []
        

  
def create_asset(asset):
    asset.id = generate_id()
    event = f"{asset.id} has been created by {asset.owner_id}. It is a {asset.type}"
    create_asset_chaincode.events.append(event)
       
        
def transfer_asset(asset, recipient, sender):
    asset.owner_id = recipient.id
    event = f"{asset.id} has been transferred from {sender.id} to {recipient.id}"
    transfer_asset_chaincode.events.append(event)
    

def read_asset(asset):
    print(asset)
    
    
def delete_asset(asset):
    del asset
    
    
def select_endorsers():
    
    from Fabric.Network import Network as FabricNetwork
    
    organization_one = FabricNetwork.organizations["1"]
    organization_two = FabricNetwork.organizations["2"]
    
    organization_one_endorser = random.choice(list(organization_one))
    organization_two_endorser = random.choice(list(organization_two))
    
    return [organization_one_endorser, organization_two_endorser]
    
    
        
    
transfer_asset_chaincode = Chaincode()
transfer_asset_chaincode.contract = transfer_asset

read_asset_chaincode = Chaincode()
read_asset_chaincode.contract = read_asset

create_asset_chaincode = Chaincode()
create_asset_chaincode.contract = create_asset

delete_asset_chaincode = Chaincode()
delete_asset_chaincode.contract = delete_asset

endorsement_policy = Chaincode()


chaincodes = [
    create_asset_chaincode,
    read_asset_chaincode,
    transfer_asset_chaincode,
    delete_asset_chaincode
]