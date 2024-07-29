from Configuration import SlimcoinConfiguration
from Statistics import get_recent_block_time

class PoB:
    
    # loses 100th of its value every minute
    decay_rate = 0.01 # 0.001 
    burn_transactions = {}
    burn_hash_target_in_hex = SlimcoinConfiguration.INITIAL_BURN_HASH_TARGET_HEX
        
    @staticmethod
    def get_total_effective_burnt_coins():
        
        from Slimcoin.BurnAddress import BurnAddress
                
        total_effective_burnt_coins = 0
        for burn_transaction in BurnAddress.burn_transactions.values():
            total_effective_burnt_coins += burn_transaction.get_effective_burnt_coins()
            
        return total_effective_burnt_coins
    
    
    # @staticmethod
    # def get_new_burn_hash_target ():
    #     previous_burn_hash_target = int(PoB.burn_hash_target_in_hex, 16)
    #     recent_block_time = get_recent_block_time()
    #     new_burn_hash_target = (previous_burn_hash_target * SlimcoinConfiguration.TARGET_BLOCK_TIME)/recent_block_time  * (SlimcoinConfiguration.REFERENCE_TOTAL_EFFECTIVE_BURNT_COINS/PoB.get_total_effective_burnt_coins())
    #     new_burn_hash_target = hex(int(new_burn_hash_target))
    #     print(f"\nNew burn hash target: {new_burn_hash_target}.\n")
    #     return new_burn_hash_target
    @staticmethod
    def get_new_burn_hash_target():
        previous_burn_hash_target = int(PoB.burn_hash_target_in_hex, 16)
        recent_block_time = get_recent_block_time()
        
        new_burn_hash_target = (
            previous_burn_hash_target *
            SlimcoinConfiguration.TARGET_BLOCK_TIME / 
            recent_block_time * 
            SlimcoinConfiguration.REFERENCE_TOTAL_EFFECTIVE_BURNT_COINS / 
            PoB.get_total_effective_burnt_coins()
        )
        
        new_burn_hash_target = hex(int(new_burn_hash_target)).rstrip('0').rstrip('x')
        if not new_burn_hash_target.startswith('0x'):
            new_burn_hash_target = '0x' + new_burn_hash_target
            
        print(f"\nNew burn hash target: {new_burn_hash_target}.\n")
        return new_burn_hash_target
        
        
    @staticmethod
    def adjust_burn_hash_target ():
        PoB.burn_hash_target_in_hex = PoB.get_new_burn_hash_target()
        
    
    @staticmethod
    def select_block_proposer():
        from Slimcoin.BurnAddress import BurnAddress
        from Slimcoin.Network import Network as SlimcoinNetwork
        
        for burn_transaction in BurnAddress.burn_transactions.values():
            if burn_transaction.meets_burn_hash_target():
                block_proposer = SlimcoinNetwork.nodes[burn_transaction.sender_id]
                BurnAddress.burn_transactions.pop(burn_transaction.id)
                return block_proposer, burn_transaction
            
        return None