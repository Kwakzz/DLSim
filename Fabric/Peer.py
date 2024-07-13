from Fabric.Node import Node as FabricNode
from Fabric.Chaincode import chaincodes

class Peer (FabricNode):
    
    def __init__(
        self, 
        id,
        blockchain=[],
        transaction_memory_pool = {},
        chaincodes = {}
    ):
        super().__init__ (id, blockchain = [])
        self.transaction_memory = transaction_memory_pool
        self.chaincodes = chaincodes
        
        
    def __str__(self):
        return f"""
        Peer {self.id}
        """
        
        
    def execute_transaction():
        pass
    
    
    def initialize_chaincodes(self):
        for chaincode in chaincodes:
            self.chaincodes[chaincode.id] = chaincode
    
    
    
    