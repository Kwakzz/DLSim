from Configuration import BitcoinConfiguration
import threading
from time import time
from Util import adjust_difficulty_target

class Consensus:
    
    winner_flag = threading.Event() # indicates whether a miner has found the PoW.
    latest_winners = []
    latest_blocks = []
    hash_attempts = 0 # attempts made in most recent competition
    
    @staticmethod
    def pow(miner, block, max_no_of_winners=3):
        
        start_time = time()
    
        while not Consensus.winner_flag.is_set() and len(Consensus.latest_winners) < max_no_of_winners:
            
            Consensus.hash_attempts += 1
            
            block.hash = miner.scan_pow(block)
            
            if block.is_pow_valid():                
                
                Consensus.winner_flag.set()
                Consensus.latest_winners.append(miner)
                Consensus.latest_blocks.append(block)
                                
                end_time = time()
                elapsed_time = end_time - start_time
                
                print(f"\nNode {miner.id} has solved the PoW in {elapsed_time} seconds.\n")
                
                miner.broadcast_block(block)
                
                Consensus.winner_flag.clear()
                break        
    
    @staticmethod   
    def competition(miners):
        
        Consensus.hash_attempts = 0
        
        start_time = time()
        
        BitcoinConfiguration.prev_elapsed_time_for_mining_round = BitcoinConfiguration.current_elapsed_time_for_mining_round
        
        threads = []
                
        miner_ids = []
        for miner in miners:
            miner_ids.append(miner.id)
        print(", ".join(miner_ids) + " are mining.")
        
        for miner in miners:
            block = miner.created_blocks.pop(-1)
            thread = threading.Thread(target=Consensus.pow, args=(miner, block))
            thread.start()
            threads.append(thread)
            
        # wait for miners to find pow before continuing program.
        for thread in threads:
            thread.join()
        
        end_time = time()
        elapsed_time_for_mining_round = end_time - start_time
        BitcoinConfiguration.current_elapsed_time_for_mining_round = elapsed_time_for_mining_round
        
        from Network import calculate_bitcoin_network_hash_rate
        calculate_bitcoin_network_hash_rate(Consensus.hash_attempts, elapsed_time_for_mining_round) 
        
        adjust_difficulty_target()
        
        

        
        