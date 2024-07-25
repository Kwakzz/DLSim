from datetime import datetime
import threading
from Configuration import GeneralConfiguration, BitcoinConfiguration, EthereumConfiguration, SlimcoinConfiguration
from Transaction import create_random_transactions
from Node import update_balances
from Util import print_chain, format_datetime
from Statistics import print_performance_statistics, record_statistics, record_time_values, plot_graphs


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
            print_performance_statistics()
            record_statistics()
            record_time_values()
            update_balances()

        
    if GeneralConfiguration.selected_platform == "Bitcoin":
        from Bitcoin.Node import assign_miners, miners_create_blocks
        from Bitcoin.Consensus import Consensus as PoW
        from Bitcoin.Network import Network as BitcoinNetwork
        from Bitcoin.Statistics import print_hashpower_statistics
        
        BitcoinNetwork.initialize_network()
        
        for round_count in range(GeneralConfiguration.no_of_rounds):
            create_random_transactions(GeneralConfiguration.TRANSACTION_COUNT_PER_ROUND)
            assign_miners()
            miners_create_blocks()
            PoW.competition_and_block_processing(BitcoinConfiguration.miners)
            PoW.reset_winners_and_blocks()
            BitcoinNetwork.clear_block_memory()
            print_chain()
            # BitcoinNetwork.set_new_difficulty()
            GeneralConfiguration.simulation_end_time = datetime.now()
            print_hashpower_statistics()
            print_performance_statistics()
            record_statistics()
            record_time_values()
            update_balances()
            
        print_hashpower_statistics()
            
        
    if GeneralConfiguration.selected_platform == "Fabric":
        
        from Fabric.Network import Network as FabricNetwork
        from Fabric.EndorsementPolicy import EndorsementPolicy
        from Fabric.Node import clients_generate_proposals, clients_submit_proposals_to_endorsing_peers, clients_assemble_endorsements_into_proposals, clients_create_transactions_from_proposals, clients_submit_transactions_to_ordering_service
        from Fabric.Peer import endorsing_peers_execute_transactions, endorsing_peers_return_proposal_responses_to_clients
        from Fabric.Consensus import Consensus as Raft


        
        FabricNetwork.initialize_network()
        FabricNetwork.select_leader()
        EndorsementPolicy.print()
        
        election_thread = threading.Thread(target=Raft.start_election)
        election_thread.start()
        
        for round_count in range(GeneralConfiguration.no_of_rounds):
            EndorsementPolicy.set_endorsers()
            clients_generate_proposals()
            clients_submit_proposals_to_endorsing_peers()
            endorsing_peers_execute_transactions()
            endorsing_peers_return_proposal_responses_to_clients()
            clients_assemble_endorsements_into_proposals()
            clients_create_transactions_from_proposals()
            if FabricNetwork.leader:
                clients_submit_transactions_to_ordering_service()
                FabricNetwork.leader.append_entries()
                # FabricNetwork.leader.print_transactions_log()
                block = FabricNetwork.leader.create_block()
                FabricNetwork.leader.broadcast_block_to_peers(block)
                print_chain()
                GeneralConfiguration.simulation_end_time = datetime.now()
                print_performance_statistics()
                record_statistics()
                record_time_values()
            else: 
                print("There's currently no leader.")
                
        Raft.stop_election = True
        election_thread.join()
            
    
    if GeneralConfiguration.selected_platform == "Slimcoin":
        
        from Slimcoin.Network import Network as SlimcoinNetwork
        from Slimcoin.Node import assign_miners, miners_burn_coins, miners_create_pow_blocks
        from Slimcoin.Consensus import Consensus as PoB
        
        
        SlimcoinNetwork.initialize_network()  
        
        for round_count in range(GeneralConfiguration.no_of_rounds):
            create_random_transactions(GeneralConfiguration.TRANSACTION_COUNT_PER_ROUND)
            assign_miners()
            miners_burn_coins()
            
            if PoB.select_block_proposer():
                block_proposer, burn_transaction = PoB.select_block_proposer()
                block = block_proposer.create_pob_block(burn_transaction)
                block_proposer.broadcast_block(block)
                if SlimcoinNetwork.verify_block(block):
                    block.finalize_transactions(block_proposer)
                    block.add_to_chain()
                    PoB.adjust_burn_hash_target()
            
            else:
                miners_create_pow_blocks()
                PoW.competition_and_block_processing(SlimcoinConfiguration.miners)
                PoW.reset_winners_and_blocks()
                SlimcoinNetwork.clear_block_memory()      
                
            print_chain()
            GeneralConfiguration.simulation_end_time = datetime.now()
            print_performance_statistics()
            record_statistics()
            record_time_values()
            update_balances()
            
        
    GeneralConfiguration.simulation_end_time = datetime.now()
    print(f"Simulation ends at {format_datetime(GeneralConfiguration.simulation_end_time)}.\n")
    print("OVERALL PERFORMANCE STATISTICS:")
    print_performance_statistics()
    plot_graphs()
    
    
if __name__ == '__main__':
    main()


    