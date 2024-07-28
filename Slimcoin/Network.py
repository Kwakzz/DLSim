import random
from Bitcoin.Network import Network as BitcoinNetwork
from Ethereum.Network import Network as EthereumNetwork
from Configuration import BitcoinConfiguration, GeneralConfiguration, SlimcoinConfiguration
from Util import get_last_block

class Network (BitcoinNetwork, EthereumNetwork):
        
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
        

    @staticmethod
    def is_pob_eligible(round_count):        
        if round_count > SlimcoinConfiguration.MINIMUM_NUMBER_OF_POW_BLOCKS_PRECEEDING_POB_BLOCK:
            if get_last_block().is_pow_block():
                return True
        
        return False
    
    
    @staticmethod
    def pos_or_pob():
        return random.choice(["PoS", "PoB"])