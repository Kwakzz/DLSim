from datetime import datetime
import threading
from Configuration import GeneralConfiguration, BitcoinConfiguration
from Transaction import create_random_transactions
from Network import Network
from Util import print_chain, format_datetime
from Statistics import generate_statistics
from Block import genesis_block


def main():
    
    Network.initialize_network()
    GeneralConfiguration.simulation_start_time = datetime.now()
    print(f"Simulation begins at {format_datetime(GeneralConfiguration.simulation_start_time)}.\n")
    
    if GeneralConfiguration.selected_platform == "Ethereum":
        from Ethereum.DepositContract import DepositContract, nodes_stake
        from Ethereum.Slot import Slot
        from Ethereum.SlashContract import SlashContract
        
        create_random_transactions()
        
        DepositContract.create()
        SlashContract.create()
        
        nodes_stake()
        DepositContract.print_deposits()
        
        Slot.slot_thread = threading.Thread(target=Slot.run_slot)
        Slot.slot_thread.start()
        
    
    for run_count in range(GeneralConfiguration.no_of_runs):
        
        create_random_transactions()
                    
        if GeneralConfiguration.selected_platform == "Bitcoin":
            from Bitcoin.Node import assign_miners, miners_create_blocks
            from Bitcoin.Consensus import Consensus as PoW
            from Bitcoin.Network import Network as BitcoinNetwork
            
            assign_miners()
            miners_create_blocks()
            PoW.competition(BitcoinConfiguration.miners)
            PoW.reset_winners_and_blocks()
            BitcoinNetwork.clear_block_memory()
            print_chain()
            BitcoinNetwork.adjust_difficulty_target()
            
            
    if GeneralConfiguration.selected_platform == "Ethereum":
        # Wait for the slot thread to complete
        Slot.slot_thread.join()
        
    GeneralConfiguration.simulation_end_time = datetime.now()
    print(f"Simulation ends at {format_datetime(GeneralConfiguration.simulation_end_time)}.\n")
    generate_statistics()
    


if __name__ == '__main__':
    main()
