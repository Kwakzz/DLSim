from Ethereum.Network import Network as EthereumNetwork
from Configuration import GeneralConfiguration, EthereumConfiguration
import random

class Consensus:
    
    def __init__(self):
        pass
    
    block_proposer = None
    
    
    @staticmethod
    def select_validators():
        EthereumNetwork.validators.clear()
        
        from Ethereum.DepositContract import DepositContract
        
        for node_id, node in EthereumNetwork.nodes.items():
            deposit = DepositContract.deposits.get(node_id, 0)
            if deposit >= 32:
                EthereumNetwork.validators[node_id] = node
                
     
    def print_validators():
        from Ethereum.DepositContract import DepositContract
        
        print("\nValidators:")
        for node in EthereumNetwork.validators.values():
            print(f"Node {node.id}: {DepositContract.deposits.get(node.id)} ETH")
            
    
class RANDAO:
    
    random_beacon = ''
    
    @staticmethod
    def generate_random_beacon():
        secret_values = []
        for validator in EthereumNetwork.validators.values():
            secret_values.append(validator.generate_secret_value())
        
        combined_secret_values = b''.join([secret_value for secret_value in secret_values])
        
        import hashlib
        random_beacon = hashlib.sha256(combined_secret_values).hexdigest()
        return random_beacon
    
    
    @staticmethod
    def print_random_beacon():
        print(f"\nRandom beacon generated for slot {str(EthereumConfiguration.current_slot)} is {RANDAO.random_beacon}.\n")
    
    
    @staticmethod
    def set_random_beacon():
        RANDAO.random_beacon = RANDAO.generate_random_beacon()
        RANDAO.print_random_beacon()
    
    
    @staticmethod
    def generate_unique_value_for_slot():
        
        from Util import sha256_hash
        return sha256_hash(RANDAO.random_beacon + str(EthereumConfiguration.current_slot))
    
    
    @staticmethod
    def select_block_proposer():
        
        from Ethereum.DepositContract import DepositContract

        pick = RANDAO.weighted_random_pick()
        
        current = 0
        for validator in EthereumNetwork.validators.values():
            current += DepositContract.deposits[validator.id]
            if current > pick:
                Consensus.block_proposer = validator
                print(f"{validator.id} has been selected as the block proposer for slot {str(EthereumConfiguration.current_slot)}.")
                return validator
    
    
    @staticmethod
    def weighted_random_pick():
        
        unique_value = RANDAO.generate_unique_value_for_slot()
        
        random.seed(int(unique_value, 16))
        
        from Ethereum.DepositContract import DepositContract
        return random.uniform(0, DepositContract.get_total_stake())
    
    
    
    
    
