import random
from Bitcoin.Network import Network as BitcoinNetwork
from Configuration import BitcoinConfiguration, GeneralConfiguration

class Network (BitcoinNetwork):
        
    @staticmethod
    def add_node():
        from Slimcoin.Node import Node as SlimcoinNode
        
        initial_balance = random.randrange(GeneralConfiguration.MINIMUM_INITIAL_BALANCE, GeneralConfiguration.MAXIMUM_INITIAL_BALANCE)
            
        hashpower_class_no = random.randrange(1, 4) 
        hashpower_class = None
        
        if hashpower_class_no == 1:
            hashpower_class = BitcoinConfiguration.LOW_HASHPOWER
        elif hashpower_class_no == 2:
            hashpower_class = BitcoinConfiguration.MEDIUM_HASHPOWER
        elif hashpower_class_no == 3:
            hashpower_class = BitcoinConfiguration.HIGH_HASHPOWER
        
        hashpower = hashpower_class
        
        node = SlimcoinNode(balance=initial_balance, hashpower=hashpower)
        Network.nodes[node.id] = node
        # print(node)
        

    