from datetime import datetime
import threading
from Configuration import GeneralConfiguration, BitcoinConfiguration, EthereumConfiguration
from Transaction import create_random_initial_transactions, create_random_transactions
from Network import Network
from Node import update_balances
from Util import print_chain, format_datetime
from Statistics import generate_overall_statistics, generate_current_statistics

# Flag to indicate when the simulation should stop
stop_simulation = threading.Event()


def main():
    
    Network.initialize_network()
    GeneralConfiguration.simulation_start_time = datetime.now()
    print(f"Simulation begins at {format_datetime(GeneralConfiguration.simulation_start_time)}.\n")


    if GeneralConfiguration.selected_platform == "Ethereum":
        from Ethereum.DepositContract import DepositContract, nodes_stake
        from Ethereum.Slot import Slot
        from Ethereum.SlashContract import SlashContract
                
        DepositContract.create()
        SlashContract.create()

        for slot in range(EthereumConfiguration.max_no_of_slots):
            create_random_transactions(GeneralConfiguration.TRANSACTION_COUNT_PER_ROUND)
            nodes_stake()
            DepositContract.print_deposits()
            Slot.run_slot()
            GeneralConfiguration.simulation_end_time = datetime.now()
            generate_current_statistics()
            update_balances()

        
    if GeneralConfiguration.selected_platform == "Bitcoin":
        from Bitcoin.Node import assign_miners, miners_create_blocks
        from Bitcoin.Consensus import Consensus as PoW
        from Bitcoin.Network import Network as BitcoinNetwork
        
        for run_count in range(GeneralConfiguration.no_of_runs):
            create_random_transactions(GeneralConfiguration.TRANSACTION_COUNT_PER_ROUND)
            assign_miners()
            miners_create_blocks()
            PoW.competition(BitcoinConfiguration.miners)
            PoW.reset_winners_and_blocks()
            BitcoinNetwork.clear_block_memory()
            print_chain()
            # BitcoinNetwork.set_new_difficulty()
            GeneralConfiguration.simulation_end_time = datetime.now()
            generate_current_statistics()
            update_balances()
            
        
    if GeneralConfiguration.selected_platform == "Fabric":
        from Fabric.Node import generate_initial_create_transaction_proposals
        
        generate_initial_create_transaction_proposals()


    stop_simulation.set()

    GeneralConfiguration.simulation_end_time = datetime.now()
    print(f"Simulation ends at {format_datetime(GeneralConfiguration.simulation_end_time)}.\n")
    generate_overall_statistics()
    
    
if __name__ == '__main__':
    main()
