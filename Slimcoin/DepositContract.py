from itertools import combinations
import random
from Configuration import EthereumConfiguration
from Ethereum.DepositContract import DepositContract as EthereumDepositContract
from Slimcoin.Network import Network as SlimcoinNetwork

class DepositContract (EthereumDepositContract):
    
    @staticmethod   
    def print_deposits():
        print("\nDeposits")
        for deposit in DepositContract.deposits.items():
            if deposit[1] != 0:
                print(f"Node {deposit[0]}: {deposit[1]} SLM")


def nodes_stake():
    
    nodes_staking = random.choice(list(combinations(SlimcoinNetwork.nodes.values(), 2)))
            
    for node in nodes_staking:
        if node.balance > 32:
            amount = random.randrange(EthereumConfiguration.MINIMUM_STAKE, EthereumConfiguration.MAXIMUM_STAKE)
            node.stake(amount)
        else:
            print(f"{node.id} doesn't have enough coins to stake.")  