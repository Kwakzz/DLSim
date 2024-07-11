from datetime import datetime
import threading
from Configuration import GeneralConfiguration, BitcoinConfiguration
from Transaction import create_random_initial_transactions, create_random_transactions
from Network import Network
from Util import print_chain, format_datetime
from Statistics import generate_statistics
from Node import update_balances

# Flag to indicate when the simulation should stop
stop_simulation = threading.Event()


# def transaction_thread():
#     while not stop_simulation.is_set():
#         create_random_transaction()
        
        
# def buy_coins_thread():
#     while not stop_simulation.is_set():
#         update_balances()


def main():
    
    Network.initialize_network()
    create_random_initial_transactions()
    GeneralConfiguration.simulation_start_time = datetime.now()
    print(f"Simulation begins at {format_datetime(GeneralConfiguration.simulation_start_time)}.\n")

    # transaction_thread_obj = threading.Thread(target=transaction_thread)
    # transaction_thread_obj.start()
    
    # buy_coins_thread_obj = threading.Thread(target=buy_coins_thread)
    # buy_coins_thread_obj.start()


    if GeneralConfiguration.selected_platform == "Ethereum":
        from Ethereum.DepositContract import DepositContract, nodes_stake
        from Ethereum.Slot import Slot
        from Ethereum.SlashContract import SlashContract

        DepositContract.create()
        SlashContract.create()

        for run_count in range(GeneralConfiguration.no_of_runs):
            nodes_stake()
            DepositContract.print_deposits()

        Slot.slot_thread = threading.Thread(target=Slot.run_slot)
        Slot.slot_thread.start()
        # Wait for the slot thread to complete
        Slot.slot_thread.join()
        
    if GeneralConfiguration.selected_platform == "Bitcoin":
        from Bitcoin.Node import assign_miners, miners_create_blocks
        from Bitcoin.Consensus import Consensus as PoW
        from Bitcoin.Network import Network as BitcoinNetwork

        for run_count in range(GeneralConfiguration.no_of_runs):

            assign_miners()
            miners_create_blocks()
            PoW.competition(BitcoinConfiguration.miners)
            PoW.reset_winners_and_blocks()
            BitcoinNetwork.clear_block_memory()
            print_chain()
            create_random_transactions(1700)
            # BitcoinNetwork.set_new_difficulty()
        
        
    if GeneralConfiguration.selected_platform == "Fabric":
        pass

    # Stop the transaction thread and wait for it to finish
    stop_simulation.set()
    # transaction_thread_obj.join()
    # buy_coins_thread_obj.join()

    GeneralConfiguration.simulation_end_time = datetime.now()
    print(f"Simulation ends at {format_datetime(GeneralConfiguration.simulation_end_time)}.\n")
    generate_statistics()
    
    
if __name__ == '__main__':
    main()
