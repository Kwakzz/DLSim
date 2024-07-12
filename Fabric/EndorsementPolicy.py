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