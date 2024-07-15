from datetime import datetime
from Configuration import GeneralConfiguration, BitcoinConfiguration, EthereumConfiguration
from Transaction import create_random_transactions
from Node import update_balances
from Util import print_chain, format_datetime
from Statistics import generate_overall_statistics, generate_current_statistics


def main():
    
    GeneralConfiguration.simulation_start_time = datetime.now()
    print(f"Simulation begins at {format_datetime(GeneralConfiguration.simulation_start_time)}.\n")


    if GeneralConfiguration.selected_platform == "Ethereum":
        from Ethereum.DepositContract import DepositContract, nodes_stake
        from Ethereum.Slot import Slot
        from Ethereum.SlashContract import SlashContract
        from Ethereum.Network import Network as EthereumNetwork
        
        EthereumNetwork.initialize_network()
                
        DepositContract.create()
        SlashContract.create()

        for slot in range(EthereumConfiguration.max_no_of_slots):
            create_random_transactions(GeneralConfiguration.TRANSACTION_COUNT_PER_ROUND)
            nodes_stake()
            DepositContract.print_deposits()
            Slot.run_slot()
            GeneralConfiguration.simulation_end_time = datetime.now()
            generate_current_statistics()
            update_balances()

        
    if GeneralConfiguration.selected_platform == "Bitcoin":
        from Bitcoin.Node import assign_miners, miners_create_blocks
        from Bitcoin.Consensus import Consensus as PoW
        from Bitcoin.Network import Network as BitcoinNetwork
        
        BitcoinNetwork.initialize_network()
        
        for round_count in range(GeneralConfiguration.no_of_rounds):
            create_random_transactions(GeneralConfiguration.TRANSACTION_COUNT_PER_ROUND)
            assign_miners()
            miners_create_blocks()
            PoW.competition(BitcoinConfiguration.miners)
            PoW.reset_winners_and_blocks()
            BitcoinNetwork.clear_block_memory()
            print_chain()
            # BitcoinNetwork.set_new_difficulty()
            GeneralConfiguration.simulation_end_time = datetime.now()
            generate_current_statistics()
            update_balances()
            
        
    if GeneralConfiguration.selected_platform == "Fabric":
        
        from Fabric.Network import Network as FabricNetwork
        from Fabric.EndorsementPolicy import EndorsementPolicy
        from Fabric.Node import clients_generate_proposals, clients_submit_proposals_to_endorsing_peers, clients_assemble_endorsements_into_proposals, clients_create_transactions_from_proposals, clients_submit_transactions_to_ordering_service
        from Fabric.Peer import endorsing_peers_execute_transactions, endorsing_peers_return_proposal_responses_to_clients


        
        FabricNetwork.initialize_network()
        
        for round_count in range(GeneralConfiguration.no_of_rounds):
            EndorsementPolicy.print()
            EndorsementPolicy.set_endorsers()
            clients_generate_proposals()
            clients_submit_proposals_to_endorsing_peers()
            endorsing_peers_execute_transactions()
            endorsing_peers_return_proposal_responses_to_clients()
            clients_assemble_endorsements_into_proposals()
            clients_create_transactions_from_proposals()
            clients_submit_transactions_to_ordering_service()
            block = FabricNetwork.leader.create_block()
            FabricNetwork.leader.broadcast_block_to_peers(block)
            print_chain()
            
            
        

    GeneralConfiguration.simulation_end_time = datetime.now()
    print(f"Simulation ends at {format_datetime(GeneralConfiguration.simulation_end_time)}.\n")
    generate_overall_statistics()
    
    
if __name__ == '__main__':
    main()
