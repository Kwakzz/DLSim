from Block import Block
from Configuration import Configuration
from Network import Network
from Transaction import Transaction
import random

if Configuration.selected_platform == "Ethereum":
    from Ethereum.Node import Node
    from Ethereum.Consensus import Consensus as Proof_of_Stake

def main ():
    
    Configuration.start_timer(10)
    
    Network.initialize_network()
    
    for run_count in range(Configuration.no_of_runs):
        
        print("\nRUN {}".format(run_count+1))
        
        for transaction_count in range (Configuration.no_of_transactions_per_round):
            transaction = Transaction()
            transaction.create_random_transaction()
            
        if Configuration.selected_platform == "Ethereum":
            
            Proof_of_Stake.staking_round()
            Proof_of_Stake.select_eligible_forgers()
            Proof_of_Stake.select_forger_by_coin_age()
            generated_block = Proof_of_Stake.forger.generate_block()
            
            if generated_block.are_transactions_valid():
                print("Block {} validated!".format(generated_block.id))
                Proof_of_Stake.forger.propagate_block(generated_block)
                Proof_of_Stake.forger.reset_stake()
            else: 
                Network.discard_block(generated_block)
                Proof_of_Stake.slash()
                
            
                
            
            
if __name__ == '__main__':
    main()
            
            
            
            
        
    
    
    