import random


available_platforms = ["Bitcoin", "Ethereum"]

class GeneralConfiguration:
        
    no_of_runs = 1
    
    overall_start_time = 0
    
    processed_transaction_count = 0
    transaction_batch_start_time = 0
    transaction_batch_end_time = 0
    
    transaction_count_per_run = 5
    
    transaction_propagation_delay = 2
    block_propagation_delay = 10
    
    maximum_initial_balance = 500
    minumum_initial_balance = 10
    
    no_of_nodes = 10
        
    selected_platform = available_platforms[1]


class EthereumConfiguration:
        
    transaction_gas = 21000 # Typical Ethereum transaction requires 21000 units of gas
    block_gas_limit = 210000
    transaction_gas = 50 # measures the computational effort required to execute a transaction.
    target_gas_usage_rate = 0.5 # 50% of maximum gas limit per block.
    target_gas_usage = target_gas_usage_rate * block_gas_limit
    
    initial_base_fee = 100 * (10**-9)
    current_base_fee = initial_base_fee
    base_fee_change_rate = 0.125
    max_tip = 20 # in gwei. 1 gwei = 1*10^-9 ETH
    
    no_of_validators_per_slot = 13 # churn limit
    validators = []
    
    current_epoch = 1
    slot_duration = 12 # 12 seconds
    current_slot = 1
    epoch_duration = slot_duration * 32
        

class BitcoinConfiguration:
    
    block_size_limit = 1000 # actual block size limit for Bitcoin is 1MB.
    
    low_power_hashpower = range(1, 6)
    medium_power_hashpower = range(6, 21)
    high_power_hashpower = range(21, 101)
        
    base_pow_time = 60 # average time it takes for a miner to perform a hash attempt
    target_block_time = 600 # average time it takes to create a block and add to the chain. set by the network to ensure consistency
    
    difficulty_target = 1
    no_of_miners = 3
    miners = []
    
    prev_total_block_time = 0 # time it takes to create all blocks in a mining round, verify and add them to the chain
    current_total_block_time = 0
    