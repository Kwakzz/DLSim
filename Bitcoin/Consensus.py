from Configuration import BitcoinConfiguration
import threading
from time import time
from Util import adjust_difficulty_target

class Consensus:
    
    winner_flag = threading.Event() # indicates whether a miner has found the PoW.
    latest_winner = None
    latest_block = None
    
    @staticmethod
    def pow(miner, block):
        
        start_time = time()
    
        while not Consensus.winner_flag.is_set():
            
            block.hash = miner.scan_pow(block)
            
            if block.is_pow_valid():
                
                Consensus.winner_flag.set()
                Consensus.latest_winner = miner
                Consensus.latest_block = block
                                
                end_time = time()
                elapsed_time = end_time - start_time
                BitcoinConfiguration.current_elapsed_time_for_finding_pow = elapsed_time
                
                print(f"\nNode {miner.id} has solved the PoW in {elapsed_time} seconds.\n")
                
                miner.broadcast_block(block)
                
                Consensus.winner_flag.clear()
                break        
    
    @staticmethod   
    def competition(miners):
        
        BitcoinConfiguration.prev_elapsed_time_for_finding_pow = BitcoinConfiguration.current_elapsed_time_for_finding_pow
        
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
        