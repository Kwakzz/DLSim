from Configuration import Configuration
from Ethereum.Node import Node
import random

class Network:
    
    nodes = []
    memory_pool = []
    
    def __init__(self):
        pass        
        
    def initialize_network(self):
        if Configuration.selected_platform == "Ethereum":
            for node_count in range (Configuration.no_of_nodes):
                random_initial_balance = random.randrange(Configuration.minumum_initial_balance, Configuration.maximum_initial_balance)
                Network.nodes[node_count] = Node(id = node_count, balance=random_initial_balance)
                
