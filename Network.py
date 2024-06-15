from Configuration import GeneralConfiguration, BitcoinConfiguration
from Statistics import hash_rates, throughputs
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
    def initialize_network():
        print(f"Welcome to a simulation of the {GeneralConfiguration.selected_platform} blockchain network.\nNodes are joing the network...\n")

        if GeneralConfiguration.selected_platform == "Bitcoin":
            from Bitcoin.Network import Network as BitcoinNetwork
            
            for node_count in range(GeneralConfiguration.no_of_nodes):
                BitcoinNetwork.add_node()
                
        if GeneralConfiguration.selected_platform == "Ethereum":
            from Ethereum.Network import Network as EthereumNetwork
            
            for node_count in range(GeneralConfiguration.no_of_nodes):
                EthereumNetwork.add_node()
         
            
    @staticmethod
    def verify_block(block, miner):
        
        if block.is_valid():
            
            block.add_to_chain()
                
            for node in Network.nodes.values():
                node.block_memory_pool.pop(block.hash)
                
            for transaction in block.transactions.values():
                transaction.finalize(miner)
                
            return True
        
        return False
                
    
    @staticmethod    
    def verify_broadcasted_blocks(broadcasted_blocks, miners):
        
        for i in range (len(broadcasted_blocks)):
            
            block = broadcasted_blocks[i]
            miner = miners[i]
            
            if Network.verify_block(block, miner):
                break   