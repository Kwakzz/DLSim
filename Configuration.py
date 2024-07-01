import random


available_platforms = ["Bitcoin", "Ethereum", ""]

class GeneralConfiguration:
        
    no_of_runs = 2
    
    simulation_start_time = None
    simulation_end_time = None
        
    initial_transaction_count = 3000
    transaction_size = range(250, 1000)
    
    block_propagation_delay = 10
    
    maximum_initial_balance = 1500
    minumum_initial_balance = 100
    
    no_of_nodes = 60
    
    base_block_propagation_delay = 1  
    network_size_factor_for_delay_increase = 0.05  
    block_size_factor_for_delay_increase = 0.01  
        
    selected_platform = available_platforms[0]
    
    
    def calculate_block_propagation_delay(network_size, block_size):
        delay = GeneralConfiguration.base_block_propagation_delay + (GeneralConfiguration.network_size_factor_for_delay_increase * network_size) + (GeneralConfiguration.block_size_factor_for_delay_increase * block_size)
        return delay


class EthereumConfiguration:
    
    transaction_propagation_delay = range(2, 5)
        
    transaction_gas = 21000 # Typical Ethereum transaction requires 21000 units of gas. measures the computational effort required to execute a transaction.
    block_gas_limit = 30000000
    target_gas_usage_rate = 0.5 # 50% of maximum gas limit per block.
    target_gas_usage = target_gas_usage_rate * block_gas_limit
    
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
    
    block_size_limit = 2**20 # actual block size limit for Bitcoin is 1MB. 2^20 bytes = 1MB
    
    transaction_propagation_delay = range(6, 10)
    
    low_power_hashpower = range(1, 6)
    medium_power_hashpower = range(6, 21)
    high_power_hashpower = range(21, 51)
        
    base_pow_time = 60 # average time it takes for a miner to perform a hash attempt
    target_block_time = 600 # average time it takes to create a block and add to the chain. set by the network to ensure consistency
    
    difficulty_target = 2
    no_of_miners = range(3, 6)
    miners = []
    
    