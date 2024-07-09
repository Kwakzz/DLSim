from Ethereum.Network import Network as EthereumNetwork

class SlashContract:
    
    slashes = {}
    events = []
    max_no_of_slashes = 3
    
    
    @staticmethod
    def create():      
        for node in EthereumNetwork.nodes.values():
            SlashContract.slashes[node.id] = 0
        event = f"Slash Contract created."
        SlashContract.events.append(event)
        print(event)
          
            
    @staticmethod   
    def print_slashes():
        print("\nSlashes")
        for slash in SlashContract.slashes.items():
            if slash[1] != 0:
                print(f"Node {slash[0]}: {slash[1]}")
                
                
    @staticmethod
    def slash(validator):
        
        from Ethereum.DepositContract import DepositContract
        
        SlashContract.slashes[validator.id] += 1
        validator.balance -= 1
        event = f"Validator {validator.id} slashed.\nTotal slashes: {SlashContract.slashes[validator.id]}\nNew Deposit: {DepositContract.deposits[validator.id]}"
        SlashContract.events.append(event)
        print(event)
        
        if SlashContract.slashes[validator.id] >= SlashContract.max_slashes:
            SlashContract.remove_validator(validator)
    
    
    @staticmethod
    def remove_validator(validator):
        if validator.id in EthereumNetwork.validators:
            del EthereumNetwork.validators[validator.id]
            del EthereumNetwork.nodes[validator.id]
            event = f"Validator {validator.id} removed from network."
            SlashContract.events.append(event)
            print(event)
    
    
    @staticmethod
    def print_events():
        print("\nSlash Events")
        for event in SlashContract.events:
            print(event)