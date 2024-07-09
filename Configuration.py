from datetime import datetime
import random


available_platforms = ["Bitcoin", "Ethereum", ""]

class GeneralConfiguration:
        
    no_of_runs = 2
    
    simulation_start_time = None
    simulation_end_time = None
        
    initial_transaction_count = 20000
    transaction_size = range(250, 1000) # in bytes
    
    block_propagation_delay = 10
    
    maximum_initial_balance = 10000000000
    minumum_initial_balance = 100000000
    
    no_of_nodes = 60
    
    base_block_propagation_delay = 1  
    network_size_factor_for_delay_increase = 0.05  
    block_size_factor_for_delay_increase = 0.01  
        
    selected_platform = available_platforms[0]
    
    
    def calculate_block_propagation_delay(network_size, block_size):
        block_size_in_kb = block_size/1024
        delay = GeneralConfiguration.base_block_propagation_delay + (GeneralConfiguration.network_size_factor_for_delay_increase * network_size) + (GeneralConfiguration.block_size_factor_for_delay_increase * block_size_in_kb)
        print(f"Propagation Delay of {delay} seconds.")
        return delay


class EthereumConfiguration:
    
    transaction_propagation_delay = range(2, 5)
        
    TRANSACTION_GAS = 21000 # Typical Ethereum transaction requires 21000 units of gas. measures the computational effort required to execute a transaction.
    BLOCK_GAS_LIMIT = 30000000
    target_gas_usage_rate = 0.5 # 50% of maximum gas limit per block.
    target_gas_usage = target_gas_usage_rate * BLOCK_GAS_LIMIT
    
    initial_base_fee = 100 * (10**-9)
    current_base_fee = initial_base_fee
    base_fee_change_rate = 0.125
    max_tip = 20 # in gwei. 1 gwei = 1*10^-9 ETH
    
    no_of_validators_per_slot = 13 # churn limit
    validators = []
    
    slot_duration = 12 # 12 seconds
    epoch_duration = slot_duration * 32
    max_no_of_slots = 5
        

class BitcoinConfiguration:
    
    BLOCK_SIZE_LIMIT = 2**20 # actual block size limit for Bitcoin is 1MB. 2^20 bytes = 1MB
    
    transaction_propagation_delay = range(6, 10)
    
    # hashpower is depicted by hashes per second.
    low_power_hashpower = 10**4  # used by CPU miners
    medium_power_hashpower = 10**6 # used by GPU miners
    high_power_hashpower = 10**12 # used by ASIC miners
            
    TARGET_BLOCK_TIME = 600 
    
    no_of_miners = range(3, 6)
    miners = []
    
    INITIAL_DIFFICULTY_TARGET_HEX = '0000fffffffffffffffffffffffffffffffffffffffffffffffffffffffffff'
    INITIAL_DIFFICULTY_TARGET = int(INITIAL_DIFFICULTY_TARGET_HEX, 16) 
    INITIAL_DIFFICULTY_LEVEL = 1
    DIFFICULTY_ADJUSTMENT_INTERVAL = 5
    
    # 0000ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    # 00000000ffff0000000000000000000000000000000000000000000000000000