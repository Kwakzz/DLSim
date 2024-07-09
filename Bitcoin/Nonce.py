import secrets
from Bitcoin.Network import Network as BitcoinNetwork

class Nonce:
    
    no_of_nonce_attempts = {}
    max_no_of_attempts_before_reset = 10000000000
    
    @staticmethod
    def generate_nonce(miner, nonce):
        nonce = 0
        if (Nonce.no_of_nonce_attempts[miner.id] == 0) or (Nonce.no_of_nonce_attempts % Nonce.max_no_of_attempts_before_reset == 0):
            nonce = secrets.randbelow(2**32)
        else: 
            nonce += 1
        return nonce
            
            
    @staticmethod
    def initialize_nonce_attempts_map(miners):
        for miner in miners:
            Nonce.no_of_nonce_attempts[miner.id] = 0
            
    
    def clear_nonce_attempts_map():
        Nonce.no_of_nonce_attempts.clear()