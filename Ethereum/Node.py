from Block import Block
from Configuration import GeneralConfiguration, EthereumConfiguration
from Node import Node as BaseNode

class Node (BaseNode):
    
    def __init__(self, id, balance):
        super().__init__(id=id, balance=balance)
        self.elapsed_stake_time_in_days = 10 # 86400*10 
        self.balance_staked = 0
        self.coin_age = self.balance_staked * self.elapsed_stake_time_in_days # (self.elapsed_stake_time/86400) 86400s make a day
        
    def generate_block(self):
        if self.memory_pool:
            total_gas_used = 0
            transactions_to_include = []
            length_of_blockchain = len(self.blockchain)
            block = Block(id=length_of_blockchain, miner_id=self.id)
            block.timestamp = GeneralConfiguration.current_time
            
            # Ensure transactions don't exceed the block's gas limit
            for transaction in self.memory_pool:
                if total_gas_used + transaction.gas <= EthereumConfiguration.block_gas_limit:
                    if transaction.gas < EthereumConfiguration.transaction_gas_limit:
                        transactions_to_include.append(transaction)
                        total_gas_used += transaction.gas
                else:
                    break
                
            block.transactions = transactions_to_include
            self.block_memory.append(block)
            print("\nBlock {} has been generated. It stores {} transactions".format(block.id, len(block.transactions)))
            return block
        
    def stake_coins(self, balance_staked):
        if balance_staked <= self.balance:
            self.balance_staked = balance_staked
            self.coin_age = self.balance_staked * (self.elapsed_stake_time/86400)
        else:
            print("Error: invalid stake")
            
    def reset_stake(self):
        self.balance_staked = 0
            
            