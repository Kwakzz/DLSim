from Configuration import GeneralConfiguration, BitcoinConfiguration
from Transaction import create_random_transactions
from Network import Network
from Util import print_chain
from Statistics import print_bitcoin_statistics, record_bitcoin_statistics

if GeneralConfiguration.selected_platform == "Bitcoin":
    from Bitcoin.Node import assign_miners, miners_create_blocks
    from Bitcoin.Consensus import Consensus as PoW


def main ():
    
    Network.initialize_network()
    
    for run_count in range(GeneralConfiguration.no_of_runs):
                    
        if GeneralConfiguration.selected_platform == "Bitcoin":
            create_random_transactions()
            assign_miners()
            miners_create_blocks()
            PoW.competition(BitcoinConfiguration.miners)
            Network.verify_broadcasted_blocks(PoW.latest_blocks, PoW.latest_winners)
            PoW.reset_winners_and_blocks()
            print_chain()
            print_bitcoin_statistics()
            record_bitcoin_statistics()
            
            
            
            
            
            
            
                
            
                
            
            
if __name__ == '__main__':
    main()
            
            
            
            
        
    
