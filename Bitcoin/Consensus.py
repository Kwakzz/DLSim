from Configuration import BitcoinConfiguration, GeneralConfiguration
import threading
from time import time
from Util import convert_seconds_to_minutes
from Bitcoin.Statistics import get_hash_rate, record_hash_rate
from Bitcoin.Network import Network as BitcoinNetwork
from Bitcoin.Nonce import Nonce

class Consensus:
    
    latest_winners = []
    latest_blocks = []
    hash_attempts = 0 # attempts made in most recent competition
    solve_time = None


    @staticmethod
    def reward_miner(miner, sender, fee):
        miner.balance += fee
        sender.balance -= fee
    
    
    @staticmethod
    def reset_winners_and_blocks():
        Consensus.latest_winners.clear()
        Consensus.latest_blocks.clear()
    
    
    @staticmethod
    def pow(miner, block, max_no_of_winners=1):
        start_time = time()
            
        while len(Consensus.latest_winners) < max_no_of_winners:
            Consensus.hash_attempts += 1
            
            block.hash, block.nonce = miner.scan_pow(block)
            
            if block.is_pow_valid():
                Consensus.latest_winners.append(miner)
                Consensus.latest_blocks.append(block)
                
                end_time = time()
                elapsed_time = (end_time - start_time)
                elapsed_time = round(elapsed_time, 2)
                Consensus.solve_time = elapsed_time
                                
                print(f"\nNode {miner.id} has solved the PoW in {elapsed_time} seconds ({convert_seconds_to_minutes(elapsed_time)} minutes).\n")
                
                miner.broadcast_block(block)
                
                if BitcoinNetwork.verify_block(block) and miner == Consensus.latest_winners[0]:
                    block.add_to_chain()
                    block.finalize_transactions(miner)
                
                break
    
    
    @staticmethod   
    def competition_and_block_processing(miners):
        Consensus.hash_attempts = 0
        
        Nonce.clear_nonce_attempts_map()
        Nonce.initialize_nonce_attempts_map(miners)
        
        start_time = time()
        threads = []
        miner_ids = [miner.id for miner in miners]
        
        print(", ".join(miner_ids) + " are mining.")
        
        for miner in miners:
            block = miner.created_blocks.pop(-1)
            thread = threading.Thread(target=Consensus.pow, args=(miner, block))
            thread.start()
            threads.append(thread)
            
        # wait for all threads to finish
        for thread in threads:
            thread.join()
        
        end_time = time()    
        elapsed_time_for_mining_round = end_time - start_time 
        
        hash_rate = get_hash_rate(Consensus.hash_attempts, elapsed_time_for_mining_round)
        record_hash_rate(hash_rate)
