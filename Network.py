from Configuration import GeneralConfiguration, BitcoinConfiguration
import random

class Network:
    
    nodes = {}
    
    def __init__(self):
        pass  
    
    
    @staticmethod
    def print_nodes():
        print("Network Nodes: ")
        for node in Network.nodes.values():
            print(node)


    @staticmethod
    def get_random_node():
        random_node = random.choice(list(Network.nodes.values()))
        return random_node
    
        
    @staticmethod
    def initialize_network():
        print(f"Welcome to a simulation of the {GeneralConfiguration.selected_platform} blockchain network.\nNodes are joing the network...\n")

        if GeneralConfiguration.selected_platform == "Bitcoin":
            from Bitcoin.Network import Network as BitcoinNetwork
            
            for node_count in range(GeneralConfiguration.NO_OF_NODES):
                BitcoinNetwork.add_node()
                
        if GeneralConfiguration.selected_platform == "Ethereum":
            from Ethereum.Network import Network as EthereumNetwork
            
            for node_count in range(GeneralConfiguration.NO_OF_NODES):
                EthereumNetwork.add_node()
            
                
    @staticmethod    
    def clear_block_memory():
         for node in Network.nodes.values():
            node.block_memory_pool.clear()