import random


class EndorsementPolicy:
    
    no_of_endorsers = 2
    one_from_each_organization = True
    majority_endorsement = True
    
    @staticmethod
    def print():
        print("""
              No of Endorsers: 2 \n
              One Endorser from each organization: True \n
              Majority endorsement: True \n
        """)
        
        
    def select_endorsers():
        
        from Fabric.Network import Network as FabricNetwork
        
        organization_one = FabricNetwork.organizations["1"]
        organization_two = FabricNetwork.organizations["2"]
        
        organization_one_endorser = random.choice(list(organization_one))
        organization_two_endorser = random.choice(list(organization_two))
        
        return [organization_one_endorser, organization_two_endorser]