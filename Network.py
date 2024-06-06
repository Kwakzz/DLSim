from Configuration import GeneralConfiguration
import random

class Network:
    
    nodes = {}
    
    
    def __init__(self):
        pass  
    
    
    def print_nodes():
        print("Network Nodes: ")
        for node in Network.nodes.values():
            print(node)
        
    
    def add_node():
        initial_balance = random.randrange(GeneralConfiguration.minumum_initial_balance, GeneralConfiguration.maximum_initial_balance)
        if GeneralConfiguration.selected_platform == "Bitcoin":
            from Bitcoin.Node import Node as BitcoinNode
            node = BitcoinNode(balance=initial_balance)
            Network.nodes[node.id] = node
            print(node)
        
    @staticmethod
    def initialize_network():
        print(f"Welcome to a simulation of the {GeneralConfiguration.selected_platform} blockchain network.\nNodes are joing the network...\n")
        for node_count in range(GeneralConfiguration.no_of_nodes):
            Network.add_node()
            
    
    def verify_block(block, miner):
        
        if block.is_valid():
            
            block.add_to_chain()
                
            for node in Network.nodes.values():
                node.block_memory_pool.pop(block.hash)
                
            for transaction in block.transactions.values():
                transaction.finalize(miner)
                                
    
            
    
        
