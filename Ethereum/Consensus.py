from Network import Network

class Consensus:
    
    eligble_forgers = []
    forger = None
    
    def __init__(self):
        pass
    
    def select_eligble_forgers():
        for node in Network.nodes:
            if node.balance_staked >= 32:
                Consensus.eligible_forgers.append[node]
         
    def select_forger_by_coin_age():
        if Consensus.eligble_forgers:
            forger = Consensus.eligble_forgers[0]
            for eligible_forger in Consensus.eligble_forgers:
                if eligible_forger.coin_age > forger.coin_age:
                    forger = eligible_forger
    
    def slash():
        Consensus.forger.balance_staked = 0