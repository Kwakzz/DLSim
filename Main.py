from Configuration import GeneralConfiguration, BitcoinConfiguration
from Transaction import create_random_transactions
from Network import Network
from Util import print_chain
from Statistics import print_bitcoin_statistics, record_bitcoin_statistics

    

def main ():
    
    Network.initialize_network()
    
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
            
            from Ethereum.DepositContract import DepositContract, nodes_stake
            from Ethereum.Consensus import Consensus as PoS
            from Ethereum.Consensus import RANDAO 
            
            DepositContract.create()
            nodes_stake()
            DepositContract.print_deposits()
            
            PoS.select_validators()
            PoS.print_validators()
            
            RANDAO.set_random_beacon()
            RANDAO.select_block_proposer()
            
        
            
            
                     
            
if __name__ == '__main__':
    main()
            
            
            
            
        
    
