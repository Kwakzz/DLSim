from Fabric.Node import Node as FabricNode
from Fabric.Chaincode import chaincodes

class Peer (FabricNode):
    
    def __init__(
        self, 
        id,
        blockchain=[],
        transaction_memory = {},
        chaincodes = {}
    ):
        super().__init__ (id, blockchain = [])
        self.transaction_memory = transaction_memory
        self.chaincodes = chaincodes
        
        
    def execute_transaction():
        pass
    
    
    def initialize_chaincodes(self):
        for chaincode in chaincodes:
            self.chaincodes[chaincode.id] = chaincode
    
    
    
    