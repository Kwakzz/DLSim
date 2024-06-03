import random
from Configuration import GeneralConfiguration, is_pow_found
from Network import Network
import threading

class Consensus:
    
    winner_flag = threading.Event() # indicates whether a miner has found the PoW.
    
    @staticmethod
    def pow(miner, block):
        while not Consensus.winner_flag.is_set():
            block_hash = miner.scan_pow(block)
            if is_pow_found(block_hash):
                Consensus.winner_flag.set()
                break
    
    @staticmethod   
    def competition(miners):
        threads = []
        for miner in miners:
            mined_block = miner.block_memory_pool.popitem[1] # popitem removes and returns the last item in a dictionary as a tuple. A miner can't have more than one block in its block memory. dict.popitem[1] returns the value of the item being popped
            thread = threading.Thread(target=Consensus.pow, args=(miner, mined_block))
            thread.start()
            threads.append(thread)
            
        # wait for miners to find pow before continuing program.
        for thread in threads:
            thread.join()
            
