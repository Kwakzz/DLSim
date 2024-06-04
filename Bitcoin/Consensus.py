from Configuration import BitcoinConfiguration
import threading

class Consensus:
    
    winner_flag = threading.Event() # indicates whether a miner has found the PoW.
    
    @staticmethod
    def pow(miner, block):
        while not Consensus.winner_flag.is_set():
            block_hash = miner.scan_pow(block)
            if is_pow_found(block_hash):
                Consensus.winner_flag.set()
                print(f"Node {miner.id} has solved the PoW.")
                break
    
    @staticmethod   
    def competition(miners):
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
            

def is_pow_found(block_hash):
    return block_hash.startswith("0"*BitcoinConfiguration.difficulty_target)