import random


class GeneralConfiguration:
        
    no_of_runs = 1
    
    processed_transaction_count = 0
    transaction_batch_start_time = 0
    transaction_batch_end_time = 0
    
    transaction_count_per_run = 60
    
    transaction_propagation_delay = 2
    block_propagation_delay = 10
    
    maximum_initial_balance = 500
    minumum_initial_balance = 10
    
    no_of_nodes = 50
        
    selected_platform = "Bitcoin"


class EthereumConfiguration:
        
    transaction_gas_limit = 21000 # maximum amount you are willing to consume on a transaction. Standard transaction gas limit is 21000 units of gas
    block_gas_limit = 210000
    transaction_gas = 50 # measures the computational effort required to execute a transaction.
    base_fee = 10 # minimum transaction fee in Ethereum
    target_size = 15000000 # the amount of cumulative gas a block takes
    
    from Configuration import GeneralConfiguration
    no_of_nodes_staking = random.randrange(GeneralConfiguration.no_of_nodes/2, GeneralConfiguration.no_of_nodes+1)
    

class BitcoinConfiguration:
    block_size_limit = 1000 # actual block size limit for Bitcoin is 1MB.
    
    low_power_hashpower = range(1, 6)
    medium_power_hashpower = range(6, 21)
    high_power_hashpower = range(21, 101)
        
    base_pow_time = 60 # average time it takes for a miner to perform a hash attempt
    target_block_time = 600 # average time it takes to create a block. set by the network to ensure consistency
    
    difficulty_target = 1
    no_of_miners = 3
    miners = []
    
    prev_elapsed_time_for_mining_round = 0
    current_elapsed_time_for_mining_round = 0
    