from Configuration import Configuration
import random

class Network:
    
    nodes = []
    
    def __init__(self):
        pass        
        
    @staticmethod
    def initialize_network():
        print("INITIALIZING NETWORK...")
        if Configuration.selected_platform == "Ethereum":
            from Ethereum.Node import Node
            for node_count in range(Configuration.no_of_nodes):
                random_initial_balance = random.randrange(Configuration.minumum_initial_balance, Configuration.maximum_initial_balance)
                Network.nodes.insert(node_count, Node(id=node_count, balance=random_initial_balance))
                print("Node {} joined the Network with a balance of {} ETH.".format(Network.nodes[node_count].id,Network.nodes[node_count].balance))

    @staticmethod
    def discard_block(block):
        for node in Network.nodes:
            node.block_memory.pop(block.id)
