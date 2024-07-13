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
       
        
def transfer_asset(asset, recipient):
    event = f"{asset.id} has been transferred from {asset.owner_id} to {recipient.id}"
    asset.owner_id = recipient.id
    transfer_asset_chaincode.events.append(event)
    

def read_asset(asset):
    print(asset)
    
    
def delete_asset(asset):
    del asset 
    
        
    
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


def initialize_all_chaincodes_on_peers():
    
    from Fabric.Network import Network as FabricNetwork
    
    for peer in FabricNetwork.peers:
        peer.initialize_chaincodes()