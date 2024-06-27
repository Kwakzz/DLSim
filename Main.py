import threading
from Configuration import GeneralConfiguration, BitcoinConfiguration
from Transaction import create_random_transactions
from Network import Network
from Util import print_chain


def main():
    
    Network.initialize_network()
    create_random_transactions()
    
    if GeneralConfiguration.selected_platform == "Ethereum":
        from Ethereum.DepositContract import DepositContract, nodes_stake
        from Ethereum.Slot import Slot
        from Ethereum.SlashContract import SlashContract
        
        DepositContract.create()
        SlashContract.create()
        print()
        
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
            from Bitcoin.Statistics import print_bitcoin_statistics, record_bitcoin_statistics

            
            assign_miners()
            miners_create_blocks()
            PoW.competition(BitcoinConfiguration.miners)
            BitcoinNetwork.verify_broadcasted_blocks(PoW.latest_blocks, PoW.latest_winners)
            PoW.reset_winners_and_blocks()
            print_chain()
            print_bitcoin_statistics()
            record_bitcoin_statistics()
            BitcoinNetwork.adjust_difficulty_target()


if __name__ == '__main__':
    main()
