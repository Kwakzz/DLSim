from itertools import combinations
import random
from Ethereum.Network import Network as EthereumNetwork
from Configuration import EthereumConfiguration

class DepositContract:
    
    deposits = {}
    
    
    @staticmethod
    def create():
        
        for node in EthereumNetwork.nodes.values():
            DepositContract.deposits[node.id] = 0
        
    
    @staticmethod   
    def print_deposits():
        print("\nDeposits")
        for deposit in DepositContract.deposits.items():
            if deposit[1] != 0:
                print(f"Node {deposit[0]}: {deposit[1]} ETH")
            
            
    @staticmethod
    def get_total_stake():
        return sum(DepositContract.deposits.values())
        
        
        
        
def nodes_stake():
    
    network_size = len(EthereumNetwork.nodes)
    nodes_staking = random.choice(list(combinations(EthereumNetwork.nodes.values(), network_size//2)))
            
    for node in nodes_staking:
        if node.balance > 5:
            amount = random.randrange(1, node.balance//2.5)
            node.stake(amount)
        else:
            print(f"{node.id} doesn't have enough coins to stake.")
            
        