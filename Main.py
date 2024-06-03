from Block import Block
from Configuration import GeneralConfiguration
from Network import Network
import random

if GeneralConfiguration.selected_platform == "Ethereum":
    from Ethereum.Node import Node
    from Ethereum.Consensus import Consensus as Proof_of_Stake
    from Ethereum.Transaction import Transaction

def main ():
    
    Network.initialize_network()
    
    for run_count in range(GeneralConfiguration.no_of_runs):
                    
        if GeneralConfiguration.selected_platform == "Bitcoin":
            pass
            
            
                
            
                
            
            
if __name__ == '__main__':
    main()
            
            
            
            
        
    
