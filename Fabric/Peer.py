from Fabric.Asset import Asset
from Fabric.EndorsementPolicy import EndorsementPolicy
from Fabric.Node import Node as FabricNode
from Fabric.Block import genesis_block

class Peer (FabricNode):
    
    def __init__(
        self, 
        id,
    ):
        super().__init__ (id)
        self.proposals_log = []
        self.simulated_proposals = []
        self.blockchain = [genesis_block]
        
        
    def __str__(self):
        return f"""
        Peer {self.id}
        """
        
    
    def execute_transaction(self, proposal):
        
        from Fabric.Transaction import Transaction
        
        try:
            asset = Asset(type=proposal.asset_type, owner_id=proposal.client_id)
            transaction = Transaction(asset=asset, client_id=proposal.client_id, nonce=proposal.nonce)
            
            if transaction:
                proposal.endorsements[self.id] = True
                # print(transaction)
                
            else:
                print("Transaction creation failed. Proposal was not endorsed.")
                
        except Exception as e:
            print(f"Transaction execution failed: {e}")
            
        self.simulated_proposals.append(proposal)
        return proposal
    
    
    def return_proposal_response_to_client(self, proposal_response):
        
        from Fabric.Network import Network as FabricNetwork
        
        client = FabricNetwork.clients[proposal_response.client_id]
        client.proposal_responses.append(proposal_response)
            
            
    def proposals_log_is_empty(self):
        return len(self.proposals_log) == 0
    
    
    def simulated_proposals_is_empty(self):
        return len(self.simulated_proposals) == 0




def endorsing_peers_execute_transactions():
    
    print("Proposals received from clients.")
    print("\nEndorsing peers are executing transactions...")
    
    # print("\nProposal Responses:")
        
    for endorsing_peer in EndorsementPolicy.endorsing_peers:
        while not endorsing_peer.proposals_log_is_empty():
            proposal = endorsing_peer.proposals_log.pop()
            simulated_proposal = endorsing_peer.execute_transaction(proposal)
            # print(simulated_proposal)
            
    print("Transactions have been executed.")
            
            
def endorsing_peers_return_proposal_responses_to_clients():
    
    print("\nEndorsing peers are returning proposal responses to clients...")
    
    for endorsing_peer in EndorsementPolicy.endorsing_peers:
        while not endorsing_peer.simulated_proposals_is_empty():
            proposal_response = endorsing_peer.simulated_proposals.pop()
            endorsing_peer.return_proposal_response_to_client(proposal_response)