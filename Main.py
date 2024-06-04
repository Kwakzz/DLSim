from Bitcoin.Consensus import Consensus as PoW
from Configuration import GeneralConfiguration, BitcoinConfiguration
from Transaction import create_random_transactions
from Bitcoin.Node import assign_miners, miners_create_blocks
from Network import Network

if GeneralConfiguration.selected_platform == "Ethereum":
    from Ethereum.Node import Node
    from Ethereum.Consensus import Consensus as Proof_of_Stake
    from Ethereum.Transaction import Transaction

def main ():
    
    Network.initialize_network()
    
    for run_count in range(GeneralConfiguration.no_of_runs):
                    
        if GeneralConfiguration.selected_platform == "Bitcoin":
            create_random_transactions()
            assign_miners()
            miners_create_blocks()
            PoW.competition(BitcoinConfiguration.miners)
            
            
            
            
                
            
                
            
            
if __name__ == '__main__':
    main()
            
            
            
            
        
    
