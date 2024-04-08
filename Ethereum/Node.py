from Node import Node as BaseNode

class Node (BaseNode):
    
    def __init__(self, id, balance):
        super().__init__(id=id, balance=balance)
        self.elapsed_stake_time = 86400*10
        self.balance_staked = 0
        self.coin_age = self.balance_staked * (self.elapsed_stake_time/86400) #86400s make a day
        
    def stake_coins(self, balance_staked):
        if balance_staked <= self.balance:
            self.balance_staked = balance_staked
            self.coin_age = self.balance_staked * (self.elapsed_stake_time/86400)
        else:
            print("Error: invalid stake")
            
    def reset_stake(self):
        self.balance_staked = 0
            
            