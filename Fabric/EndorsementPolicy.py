import random


class EndorsementPolicy:
    
    no_of_endorsers = 2
    one_from_each_organization = True
    majority_endorsement = True
    
    @staticmethod
    def print():
        print("Endorsement Policy:")
        print("""
        No of Endorsers: 2 
        One Endorser from each organization: True 
        Majority endorsement: True
        Number of leader nodes: 1
        """)
        print()
        
        
    def select_endorsers():
        
        from Fabric.Network import Network as FabricNetwork
        
        organization_one = FabricNetwork.organizations["1"]
        organization_two = FabricNetwork.organizations["2"]
        
        organization_one_endorser = random.choice(list(organization_one))
        organization_two_endorser = random.choice(list(organization_two))
        
        print(f"{organization_one_endorser.id} and {organization_two_endorser.id} have been selected as endorsers.")
        
        return [organization_one_endorser, organization_two_endorser]