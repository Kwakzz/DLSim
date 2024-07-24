from Configuration import SlimcoinConfiguration
from Statistics import get_recent_block_time

class Consensus:
    
    # loses 100th of its value every minute
    decay_rate = 0.01 # 0.001 
    burn_transactions = {}
    burn_hash_target_in_hex = SlimcoinConfiguration.INITIAL_BURN_HASH_TARGET_HEX
        
    
    def get_total_effective_burnt_coins():
        
        from Slimcoin.Network import Network as SlimcoinNetwork
        
        random_node = SlimcoinNetwork.get_random_node()
        
        total_effective_burnt_coins = 0
        for burn_transaction in random_node.burn_transactions_memory_pool.values():
            total_effective_burnt_coins += burn_transaction.get_effective_burnt_coins()
            
        return total_effective_burnt_coins
    
    
    def get_new_burn_hash_target ():
        previous_burn_hash_target = int(Consensus.burn_hash_target_in_hex, 16)
        recent_block_time = get_recent_block_time()
        new_burn_hash_target = (previous_burn_hash_target * SlimcoinConfiguration.TARGET_BLOCK_TIME)/recent_block_time  * (SlimcoinConfiguration.REFERENCE_TOTAL_EFFECTIVE_BURNT_COINS/Consensus.get_total_effective_burnt_coins())
        new_burn_hash_target = hex(int(new_burn_hash_target))
        return new_burn_hash_target
        
        
    def adjust_burn_hash_target ():
        Consensus.burn_hash_target_in_hex = Consensus.get_new_burn_hash_target()
        
        
    def select_block_proposer():
        from Slimcoin.Network import Network as SlimcoinNetwork
        
        random_node = SlimcoinNetwork.get_random_node()
        
        for burn_transaction in random_node.burn_transactions_memory_pool.values():
            if burn_transaction.meets_burn_hash_target():
                burn_transaction.set_burn_hash()
                block_proposer = SlimcoinNetwork.nodes[burn_transaction.sender_id]
                return block_proposer, burn_transaction
            
        return None