import random
from Configuration import FabricConfiguration
from Fabric.EndorsementPolicy import EndorsementPolicy
from Util import sha256_hash

class Proposal:
    
    def __init__(self, client_id, nonce, asset_type):
        self.client_id = client_id
        self.asset_type = asset_type
        self.nonce = nonce
        self.endorsements = {}
        
    def __str__(self):
        return f"""
        Proposal (
           client: {self.client_id},
           asset: {self.asset_type}, 
           nonce: {self.nonce}
           endorsements: {self.endorsements}
        )
        """
        
        
    def has_majority_endorsement(self):
        
        no_of_endorsements = len(self.endorsements)
        endorsement_threshold = len(EndorsementPolicy.endorsing_peers) // 2 # more than half of endorsing peers must endorse a transaction for it to be valid.
        
        return no_of_endorsements > endorsement_threshold
        