from Block import Block
from Configuration import Configuration
from Network import Network
from Transaction import Transaction

if Configuration.selected_platform == "Ethereum":
    from Ethereum.Node import Node
    from Ethereum.Consensus import Consensus as Proof_of_Stake

def main ():
    
    Network.initialize_network()
    
    for run_count in range(Configuration.no_of_runs):
        
        for transaction_count in range (Configuration.no_of_transactions_per_round):
            transaction = Transaction()
            transaction.create_random_transaction()
            
        if Configuration.selected_platform == "Ethereum":
            Proof_of_Stake.select_eligble_forgers()
            Proof_of_Stake.select_forger_by_coin_age()
            
        
    
    
    