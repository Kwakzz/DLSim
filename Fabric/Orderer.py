from Fabric import Node as BaseNode

class Orderer (BaseNode):
    
    def __init__(
        self, 
        id,
        blockchain=[],
    ):
        super().__init__ (id, blockchain = [])


    def __str__(self):
        return f"""
        Orderer {self.id}
        """

    