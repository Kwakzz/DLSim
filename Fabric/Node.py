import random
from Fabric.Asset import Asset
from Fabric.EndorsementPolicy import EndorsementPolicy
from Fabric.Proposal import Proposal        
from Configuration import FabricConfiguration, GeneralConfiguration


class Node:
    
    def __init__(self, id):
        self.id = id
        self.generated_proposals = []
        self.proposal_responses = []
        self.generated_transactions = []
                        
        
    def __str__(self):
        return f"""
        Client {self.id}
        """
        
        
    def __eq__(self, other):
        if not isinstance (other, Node):
            return False
        return self.id == other.id 
        
        
    def generate_proposal(self):
                
        asset_type = random.choice(FabricConfiguration.ASSET_TYPES)
        
        proposal = Proposal(
            client_id=self.id,
            asset_type=asset_type,
            nonce=FabricConfiguration.proposal_counter
        )
        
        FabricConfiguration.proposal_counter += 1
        self.generated_proposals.append(proposal)
        return proposal
    
    
    def create_transaction(self, proposal):
        
        from Fabric.Transaction import Transaction
        
        asset = Asset(type=proposal.asset_type, owner_id=proposal.client_id)
        transaction = Transaction(asset=asset, client_id=proposal.client_id, nonce=proposal.nonce)
        transaction.set_transaction_id()
        self.generated_transactions.append(transaction)
        return transaction
        
        
    def assemble_endorsements_into_proposals(self):
        for proposal in self.generated_proposals:
            for proposal_response in list(self.proposal_responses):
                if proposal_response.nonce == proposal.nonce:
                    endorsing_peer_id = next(iter(proposal_response.endorsements.keys()))
                    proposal.endorsements[endorsing_peer_id] = True
                    self.proposal_responses.remove(proposal_response)
        
    
    def submit_proposal_to_endorsing_peers(self, proposal):
                        
        for endorsing_peer in EndorsementPolicy.endorsing_peers:
            endorsing_peer.proposals_log.append(proposal)
            
            
    def submit_transaction_to_ordering_service(self, transaction):
        
        from Fabric.Network import Network as FabricNetwork
        
        FabricNetwork.leader.transactions_log.append(transaction)
        
        
    def generated_proposals_is_empty(self):
        return len(self.generated_proposals) == 0
        
        
    def proposal_responses_is_empty(self):
        return len(self.proposal_responses) == 0
    
    
    def generated_transactions_is_empty(self):
        return len(self.generated_transactions) == 0
            
            
            
def clients_generate_proposals():
    
    from Fabric.Network import Network as FabricNetwork
        
    print("Clients are generating proposals...")
    proposal_count = 0
    
    for i in range(GeneralConfiguration.TRANSACTION_COUNT_PER_ROUND):
        client = random.choice(list(FabricNetwork.clients.values()))
        proposal = client.generate_proposal()
        proposal_count += 1
        # print(proposal)
        
    print(f"{proposal_count} proposals generated.\n")
        
        
def clients_submit_proposals_to_endorsing_peers():
    from Fabric.Network import Network as FabricNetwork
        
    print("Clients are submitting the generated proposals to endorsing peers...")
    
    for client in FabricNetwork.clients.values():
        for proposal in client.generated_proposals:
            client.submit_proposal_to_endorsing_peers(proposal) 
            
            
def clients_assemble_endorsements_into_proposals():
    
    print("Clients are assembling endorsements into proposals...")
    
    from Fabric.Network import Network as FabricNetwork
    
    for client in FabricNetwork.clients.values():
        client.assemble_endorsements_into_proposals()
    
        
def clients_create_transactions_from_proposals():
    
    from Fabric.Network import Network as FabricNetwork
    
    majority_endorsement_count = 0
        
    print("Clients are creating transactions from proposal responses...")
    
    for client in FabricNetwork.clients.values():
        while not client.generated_proposals_is_empty():
            proposal = client.generated_proposals.pop()
            if proposal.has_majority_endorsement():
                majority_endorsement_count += 1
                transaction = client.create_transaction(proposal)
                # print(transaction)
                
    print(f"{majority_endorsement_count} transactions have majority endorsement.")
        

def clients_submit_transactions_to_ordering_service():
    
    from Fabric.Network import Network as FabricNetwork
    
    print("Clients are submitting transactions to the ordering service...")
    
    for client in FabricNetwork.clients.values():
        while not client.generated_transactions_is_empty():
            transaction = client.generated_transactions.pop()
            client.submit_transaction_to_ordering_service(transaction)
    