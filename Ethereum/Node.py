from Block import Block
from Configuration import GeneralConfiguration, EthereumConfiguration
from Node import Node as BaseNode

class Node (BaseNode):
    
    def __init__(self):
        super().__init__()
        