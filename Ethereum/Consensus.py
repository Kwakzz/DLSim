from Network import Network
from Configuration import Configuration
import random

class Consensus:
    
    eligible_forgers = []
    forger = None
    
    def __init__(self):
        pass
    
    @staticmethod
    def select_eligible_forgers():
        print("\nFORGING ROUND...")
        for node in Network.nodes:
            if node.balance_staked >= 32:
                Consensus.eligible_forgers.append(node)  
                print("Node {} is an eligible forger.".format(node.id))
        return Consensus.eligible_forgers

    @staticmethod
    def select_forger_by_coin_age():
        if Consensus.eligible_forgers:
            forger = Consensus.eligible_forgers[0]
            for eligible_forger in Consensus.eligible_forgers:
                if eligible_forger.coin_age > forger.coin_age:
                    forger = eligible_forger
                    
            Consensus.forger = forger
            print("\nNode {} has been selected to forge the next block.".format(Consensus.forger.id))
            return Consensus.forger
        
                

    @staticmethod
    def staking_round():
        print("\nSTAKING ROUND...")
        for node_count in range(Configuration.no_of_nodes_staking):
            balance_staked = random.randrange(Network.nodes[node_count].balance // 2, Network.nodes[node_count].balance + 1)
            Network.nodes[node_count].stake_coins(balance_staked)
            print("Node {} staked {} ETH.".format(Network.nodes[node_count].id, balance_staked))
                    
    @staticmethod
    def slash():
        if Consensus.forger:
            Consensus.forger.balance_staked = 0
            print("Forger with ID {} was caught being dishonest. Stake has been slashed.".format(Consensus.forger.id))
