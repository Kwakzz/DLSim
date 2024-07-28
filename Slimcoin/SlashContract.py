from Ethereum.SlashContract import SlashContract as EthereumSlashContract
from Slimcoin.Network import Network as SlimcoinNetwork

class SlashContract (EthereumSlashContract):
    
    @staticmethod
    def create():      
        for node in SlimcoinNetwork.nodes.values():
            SlashContract.slashes[node.id] = 0
        event = f"Slash Contract created."
        SlashContract.events.append(event)
        print(event)
        
        
    @staticmethod
    def slash(validator):
        
        from Slimcoin.DepositContract import DepositContract
        
        SlashContract.slashes[validator.id] += 1
        validator.balance -= 1
        event = f"Validator {validator.id} slashed.\nTotal slashes: {SlashContract.slashes[validator.id]}\nNew Deposit: {DepositContract.deposits[validator.id]}"
        SlashContract.events.append(event)
        print(event)
        
        if SlashContract.slashes[validator.id] >= SlashContract.max_slashes:
            SlashContract.remove_validator(validator)
        
    
    @staticmethod
    def remove_validator(validator):
        if validator.id in SlimcoinNetwork.validators:
            del SlimcoinNetwork.validators[validator.id]
            del SlimcoinNetwork.nodes[validator.id]
            event = f"Validator {validator.id} removed from network."
            SlashContract.events.append(event)
            print(event)