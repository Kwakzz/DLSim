import random


class GeneralConfiguration:
        
    no_of_runs = 1
    
    no_of_transactions_per_round = 30
    no_of_pending_transactions = 0
    transaction_count_per_run = 10
    
    maximum_initial_balance = 200
    minumum_initial_balance = 10
    
    no_of_nodes = 10
        
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
    block_size_limit = 144 # actual block size limit for Bitcoin is 1MB.
    maximum_hashpower = 100
    minimum_hashpower = 20
    difficulty_target = 1
    no_of_miners = 3
    miners = []
    