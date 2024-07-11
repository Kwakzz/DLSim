from Fabric.Asset import Asset


class Chaincode:
    
    def __init__(self):
        self.endorsers = {}
        self.contract = None
        self.events = []


def generate_asset_id():
    
    import os

    random_bytes = os.urandom(6)
    node_id_in_hex = random_bytes.hex()
    return node_id_in_hex

  
def create_asset(type, owner):
    asset_id = generate_asset_id()
    asset = Asset(id=asset_id, type=type, owner_id=owner.id)   
    return asset
       
        
        
def transfer_asset(asset, recipient, sender):
    asset.owner_id = recipient.id
    event = f"{asset.id} has been transferred from {sender.id} to {recipient.id}"
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


