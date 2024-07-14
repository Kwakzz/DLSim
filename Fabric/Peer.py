from Fabric.Asset import Asset
from Fabric.Node import Node as FabricNode
from Fabric.Chaincode import chaincodes
from Fabric.Transaction import CreateTransaction, ReadTransaction, DeleteTransaction, TransferTransaction

class Peer (FabricNode):
    
    def __init__(
        self, 
        id,
    ):
        super().__init__ (id)
        self.chaincodes = {}
        
        
    def __str__(self):
        return f"""
        Peer {self.id}
        """
        
        
    def execute_transaction(self, transaction, test_mode=True):
        if test_mode:
            
            if transaction.chaincode:
                
                try:
                    contract = transaction.chaincode.contract
                    
                    if isinstance(transaction, CreateTransaction):
                        asset = Asset(type=transaction.asset.type, owner_id=transaction.owner.id)
                        contract(asset)
                        transaction.endorsements[self.id] = True
                        return True
                    
                    elif isinstance(transaction, ReadTransaction) or isinstance(transaction, DeleteTransaction):
                        asset = transaction.asset 
                        contract(asset)
                        transaction.endorsements[self.id] = True
                        return True
                    
                    elif isinstance(transaction, TransferTransaction):
                        asset = transaction.asset
                        recipient = transaction.recipient
                        contract(asset, recipient)
                        transaction.endorsements[self.id] = True
                        return True
                    
                    else:
                        print("Unsupported transaction type for test mode.")
                        return False
                    
                except Exception as e:
                    print(f"Transaction execution failed: {e}")
                    return False
                
            else:
                print("No contract found for this transaction.")
                transaction.is_endorsed = False
                return False
            
        else:
            # Actual execution: Implement the actual transaction execution logic here
            pass

    
    
    def initialize_chaincodes(self):
        for chaincode in chaincodes:
            self.chaincodes[chaincode.id] = chaincode
            
            
    


