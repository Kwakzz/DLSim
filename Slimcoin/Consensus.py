class Consensus:
    
    # loses 100th of its value every minute
    decay_rate = 0.01 # 0.001 
    burn_transactions = {}
        
    
    
    
    # @staticmethod
    # def select_block_proposer():
        
    #     from Ethereum.DepositContract import DepositContract

    #     pick = RANDAO.weighted_random_pick()
        
    #     current_deposit_sum = 0
    #     for validator in EthereumNetwork.validators.values():
    #         current_deposit_sum += DepositContract.deposits[validator.id]
    #         if current_deposit_sum > pick:
    #             Consensus.block_proposer = validator
    #             print(f"{validator.id} has been selected as the block proposer for slot {str(Slot.current_slot_number)}.")
    #             return validator
    