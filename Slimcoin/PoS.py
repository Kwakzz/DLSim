from Slimcoin.Network import Network as SlimcoinNetwork
from Slimcoin.Slot import Slot
from Slimcoin.DepositContract import DepositContract
from Ethereum.Consensus import RANDAO as EthereumRANDAO
from Ethereum.Consensus import Consensus as EthereumConsensus
import random

class PoS (EthereumConsensus):

        
    @staticmethod
    def update_validators_list():
                
        for node_id, node in SlimcoinNetwork.nodes.items():
            deposit = DepositContract.deposits.get(node_id, 0)
            if deposit >= 32:
                SlimcoinNetwork.validators[node_id] = node
                
     
    @staticmethod
    def print_validators():
        
        print("\nValidators:")
        for node in SlimcoinNetwork.validators.values():
            print(f"Node {node.id}: {DepositContract.deposits.get(node.id)} ETH")
            
            
    @staticmethod
    def verify_block(block):
        
        for node in SlimcoinNetwork.nodes.values():
            node.block_memory_pool.pop(block.hash)
        
        if block.is_valid():
            return True
        
        print(f"Invalid block {block.hash} detected")
        return False
        
    
class RANDAO (EthereumRANDAO):
    
        
    @staticmethod
    def generate_random_beacon():
        secret_values = []
        for validator in SlimcoinNetwork.validators.values():
            secret_values.append(validator.generate_secret_value())
        
        combined_secret_values = b''.join([secret_value for secret_value in secret_values])
        
        import hashlib
        random_beacon = hashlib.sha256(combined_secret_values).hexdigest()
        return random_beacon
    
    
    @staticmethod
    def print_random_beacon():
        print(f"\nRandom beacon generated for slot {str(Slot.current_slot_number)} is {RANDAO.random_beacon}.\n")

    
    
    @staticmethod
    def generate_unique_value_for_slot():
        
        from Util import sha256_hash
        return sha256_hash(RANDAO.random_beacon + str(Slot.current_slot_number))
    
    
    @staticmethod
    def select_block_proposer():
        
        from Slimcoin.DepositContract import DepositContract

        pick = RANDAO.weighted_random_pick()
        
        current_deposit_sum = 0
        for validator in SlimcoinNetwork.validators.values():
            current_deposit_sum += DepositContract.deposits[validator.id]
            if current_deposit_sum > pick:
                PoS.block_proposer = validator
                print(f"{validator.id} has been selected as the block proposer for slot {str(Slot.current_slot_number)}.")
                return validator
    
    
    @staticmethod
    def weighted_random_pick():
        
        unique_value = RANDAO.generate_unique_value_for_slot()
        
        random.seed(int(unique_value, 16))
        
        from Slimcoin.DepositContract import DepositContract
        return random.uniform(0, DepositContract.get_total_stake())
    
    
    
    
    
