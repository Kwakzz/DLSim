import random
from Network import Network as BaseNetwork
from Configuration import EthereumConfiguration, GeneralConfiguration

class Network (BaseNetwork):
    
    validators = {}
    
    @staticmethod
    def add_node():    
        from Ethereum.Node import Node as EthereumNode
        
        initial_balance = random.randrange(GeneralConfiguration.MINIMUM_INITIAL_BALANCE, GeneralConfiguration.MAXIMUM_INITIAL_BALANCE)
        node = EthereumNode(balance=initial_balance)
        Network.nodes[node.id] = node
        # print(node)


    @staticmethod
    def adjust_base_fee(latest_block):
        target_gas_usage = latest_block.target_gas_usage
        gas_deviation = latest_block.gas_used = latest_block.target_gas_usage
        base_fee_change_rate = EthereumConfiguration.base_fee_change_rate
        current_base_fee = EthereumConfiguration.current_base_fee
        new_base_fee = current_base_fee * (1+ (gas_deviation/target_gas_usage) * base_fee_change_rate)
        EthereumConfiguration.current_base_fee = new_base_fee
        print(f"Adjusted Base Fee: {new_base_fee} ETH")
        return new_base_fee
    
    
    
    
    
    