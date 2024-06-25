import threading
from Configuration import GeneralConfiguration, BitcoinConfiguration
from Transaction import create_random_transactions
from Network import Network
from Util import print_chain
from Statistics import print_bitcoin_statistics, record_bitcoin_statistics

    

def main ():
    
    Network.initialize_network()
    
    if GeneralConfiguration.selected_platform == "Ethereum":
        from Ethereum.DepositContract import DepositContract, nodes_stake
        from Ethereum.Slot import Slot
        
        DepositContract.create()
        
    
    for run_count in range(GeneralConfiguration.no_of_runs):
        
        create_random_transactions()
                    
        if GeneralConfiguration.selected_platform == "Bitcoin":
            
            from Bitcoin.Node import assign_miners, miners_create_blocks
            from Bitcoin.Consensus import Consensus as PoW
            
            assign_miners()
            miners_create_blocks()
            PoW.competition(BitcoinConfiguration.miners)
            Network.verify_broadcasted_blocks(PoW.latest_blocks, PoW.latest_winners)
            PoW.reset_winners_and_blocks()
            print_chain()
            print_bitcoin_statistics()
            record_bitcoin_statistics()
            
            
        if GeneralConfiguration.selected_platform == "Ethereum":
            
            nodes_stake()
            DepositContract.print_deposits()
            
          
            Slot.slot_thread = threading.Thread(target=Slot.run_slot)
            Slot.slot_thread.start()
            
            
                  
            
if __name__ == '__main__':
    main()
            
            
            
            
        
    
