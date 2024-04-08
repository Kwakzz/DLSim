import random
import time
import threading

class Configuration:
    
    current_time = 0
    no_of_runs = 3
    
    block_limit = 80000
    transaction_gas = 50
    
    no_of_transactions_per_round = 30
    
    maximum_initial_balance = 200
    minumum_initial_balance = 10
    
    no_of_nodes = 50
    no_of_nodes_staking = random.randrange(no_of_nodes/2, no_of_nodes+1)
    maximum_hashpower = 100
    minimum_hashpower = 20
    
    selected_platform = "Ethereum"
    
    @staticmethod
    def run_timer(duration):
        start_time = time.time()
        end_time = start_time + duration
        while time.time() < end_time:
            Configuration.current_time += 1
            time.sleep(1)  # Sleep for 1 second between updates

    # Define a function to start the timer in a separate thread
    @staticmethod
    def start_timer(duration):
        timer_thread = threading.Thread(target=Configuration.run_timer, args=(duration,))
        timer_thread.start()

