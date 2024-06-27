from Configuration import BitcoinConfiguration, GeneralConfiguration
import threading
from time import time
from Util import convert_seconds_to_minutes

class Consensus:
    
    latest_winners = []
    latest_blocks = []
    hash_attempts = 0 # attempts made in most recent competition
    
    
    @staticmethod
    def reward_miner(miner, sender, fee):
        miner.balance += fee
        sender.balance -= fee
    
    
    @staticmethod
    def reset_winners_and_blocks():
        Consensus.latest_winners.clear
        Consensus.latest_blocks.clear
    
    
    @staticmethod
    def pow(miner, block, max_no_of_winners=3):
        
        start_time = time()
    
        while len(Consensus.latest_winners) <= max_no_of_winners:
            
            Consensus.hash_attempts += 1
            
            block.hash, block.nonce = miner.scan_pow(block)
            
            if block.is_pow_valid():                
                
                Consensus.latest_winners.append(miner)
                Consensus.latest_blocks.append(block)
                                                
                end_time = time()
                elapsed_time = end_time - start_time # block propagation time
                
                GeneralConfiguration.processed_transaction_count += len(block.transactions)
                
                print(f"\nNode {miner.id} has solved the PoW in {elapsed_time} seconds ({convert_seconds_to_minutes(elapsed_time)} minutes).\n")
        
                miner.broadcast_block(block)
                
                break        
    
    @staticmethod   
    def competition(miners):
                
        Consensus.hash_attempts = 0
        
        start_time = time()
                
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
        BitcoinConfiguration.elapsed_time_for_mining_round = end_time - start_time         