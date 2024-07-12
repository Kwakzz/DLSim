from Fabric import Node as BaseNode

class Orderer (BaseNode):
    
    def __init__(
        self, 
        id,
        blockchain=[],
    ):
        super().__init__ (id, blockchain = [])


    