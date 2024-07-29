import random
import threading
from time import sleep
from Fabric.Network import Network as FabricNetwork
from Configuration import FabricConfiguration

class Consensus:
    
    elections = {}
    term_number = 1
    stop_election = False
    
    
    @staticmethod
    def get_random_candidate():
        FabricNetwork.reset_orderer_statuses_to_follower()
        candidate = random.choice(list(FabricNetwork.get_followers().values()))
        return candidate
    
    
    @staticmethod
    def election():
        
        print("An election has begun.")
        
        FabricNetwork.leader = None
        
        while not FabricNetwork.leader:
            candidate = Consensus.get_random_candidate()
            no_of_votes = candidate.request_votes()
            if Consensus.votes_reached_quorum(no_of_votes):
                
                print(f"{candidate.id} received {no_of_votes} votes.")
                FabricNetwork.leader = candidate
                candidate.status = FabricConfiguration.ORDERER_TYPES[2]
                
                Consensus.elections[Consensus.term_number] = candidate
                
                Consensus.term_number += 1
                print(f"\n{candidate.id} is the new leader. Term {Consensus.term_number} has begun.\n")
        
    
    @staticmethod
    def votes_reached_quorum(no_of_votes):
        return no_of_votes > FabricNetwork.get_follower_quorum() or no_of_votes == FabricNetwork.get_follower_quorum()
        
        
    @staticmethod
    def start_election():
        while not Consensus.stop_election:
            sleep(FabricConfiguration.LEADER_TIMEOUT)
            FabricNetwork.leader = None
            election_thread = threading.Thread(target=Consensus.election)
            election_thread.start()