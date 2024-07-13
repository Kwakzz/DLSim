from datetime import datetime
import random


available_platforms = ["Bitcoin", "Ethereum", "Fabric"]

class GeneralConfiguration:
        
    no_of_runs = 20
    
    simulation_start_time = None
    simulation_end_time = None
        
    INITIAL_TRANSACTION_COUNT = 2000
    transaction_size = range(250, 1000) # in bytes
    
    block_propagation_delay = 10
    
    MAXIMUM_INITIAL_BALANCE = 10000000000
    MINIMUM_INITIAL_BALANCE = 100000000
    
    NO_OF_NODES = 60
    
    BASE_BLOCK_PROPAGATION_DELAY = 1  
    NETWORK_SIZE_FACTOR_FOR_BLOCK_PROPAGATION_DELAY_INCREASE = 0.05  
    BLOCK_SIZE_FACTOR_FOR_BLOCK_PROPAGATION_DELAY_INCREASE = 0.01  
        
    selected_platform = available_platforms[1]
    
    
    def calculate_block_propagation_delay(network_size, block_size):
        block_size_in_kb = block_size/1024
        delay = GeneralConfiguration.BASE_BLOCK_PROPAGATION_DELAY + (GeneralConfiguration.NETWORK_SIZE_FACTOR_FOR_BLOCK_PROPAGATION_DELAY_INCREASE * network_size) + (GeneralConfiguration.BLOCK_SIZE_FACTOR_FOR_BLOCK_PROPAGATION_DELAY_INCREASE * block_size_in_kb)
        delay = round(delay, 2)
        return delay


class EthereumConfiguration:
    
    transaction_propagation_delay = range(2, 5)
        
    TRANSACTION_GAS = 21000 # Typical Ethereum transaction requires 21000 units of gas. measures the computational effort required to execute a transaction.
    BLOCK_GAS_LIMIT = 30000000
    TARGET_GAS_USAGE_RATE = 0.5 # 50% of maximum gas limit per block.
    target_gas_usage = TARGET_GAS_USAGE_RATE * BLOCK_GAS_LIMIT
    
    INITIAL_BASE_FEE = 100 * (10**-9)
    current_base_fee = INITIAL_BASE_FEE
    base_fee_change_rate = 0.125
    max_tip = 20 # in gwei. 1 gwei = 1*10^-9 ETH
    
    no_of_validators_per_slot = 13 # churn limit
    validators = []
    
    slot_duration = 12 # 12 seconds
    epoch_duration = slot_duration * 32
    max_no_of_slots = 20
        
    MINIMUM_STAKE = 32
    MAXIMUM_STAKE = 90


class BitcoinConfiguration:
    
    BLOCK_SIZE_LIMIT = 2**20 # actual block size limit for Bitcoin is 1MB. 2^20 bytes = 1MB
    
    transaction_propagation_delay = range(6, 10)
    
    # hashpower is depicted by hashes per second.
    LOW_HASHPOWER = 10**4  # used by CPU miners
    MEDIUM_HASHPOWER = 10**6 # used by GPU miners
    HIGH_HASHPOWER = 10**12 # used by ASIC miners
            
    TARGET_BLOCK_TIME = 600 
    
    no_of_miners = range(3, 6)
    miners = []
    
    INITIAL_DIFFICULTY_TARGET_HEX = '00000ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff'
    INITIAL_DIFFICULTY_TARGET = int(INITIAL_DIFFICULTY_TARGET_HEX, 16) 
    INITIAL_DIFFICULTY_LEVEL = 1
    DIFFICULTY_ADJUSTMENT_INTERVAL = 5
    
    # 0000ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    # 00000000ffff0000000000000000000000000000000000000000000000000000
    
    
class FabricConfiguration:
    
    INITIAL_PROPOSAL_COUNT = 900000
    
    NO_OF_ORGANIZATIONS = 2
    NO_OF_CLIENTS = 10
    NO_OF_PEERS_PER_ORGANIZATION = 2
    NO_OF_ORDERERS = 3
    
    TRANSACTION_TYPES = ["create", "read", "transfer", "delete"]
    ASSET_TYPES = ["vehicle", "house", "phone", "television"]
    
    proposal_counter = 0
    
    