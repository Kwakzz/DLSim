from Ethereum.Network import Network as EthereumNetwork
from Configuration import GeneralConfiguration, EthereumConfiguration
import random

class Consensus:
    
    def __init__(self):
        pass
    
    
    @staticmethod
    def select_validators():
        EthereumNetwork.validators.clear()
        
        from Ethereum.DepositContract import DepositContract
        
        for node_id, node in EthereumNetwork.nodes.items():
            deposit = DepositContract.deposits.get(node_id, 0)
            if deposit >= 32:
                EthereumNetwork.validators[node_id] = node
                
     
    def print_validators():
        from Ethereum.DepositContract import DepositContract
        
        print("\nValidators:")
        for node in EthereumNetwork.validators.values():
            print(f"{node.id}: {DepositContract.deposits.get(node.id)}")
            
    
class RANDAO:
    
    @staticmethod
    def generate_random_number():
        pass