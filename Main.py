from Block import Block
from Configuration import GeneralConfiguration
from Transaction import create_random_transactions
from Bitcoin.Node import assign_miners
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
            
            
            
                
            
                
            
            
if __name__ == '__main__':
    main()
            
            
            
            
        
    
