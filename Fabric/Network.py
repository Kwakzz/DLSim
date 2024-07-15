import random
from Fabric.Node import Node
from Fabric.Orderer import Orderer
from Fabric.Peer import Peer
from Util import generate_id
from Configuration import FabricConfiguration 


class Network:
    
    clients = {}
    peers = {}
    orderers = {}
    organizations = {}
    leader = None
    
    
    @staticmethod
    def initialize_network():
        print("Authorized nodes are joining the network...")
        Network.initialize_clients()
        Network.initialize_organizations()
        Network.initialize_orderers()
        Network.select_leader()
        
        
    @staticmethod
    def print_network():
        print(f""" 
        Clients: {len(Network.clients)}
        Organizations: {len(Network.organizations)}
        Peers: {len(Network.peers)}
        Orderers: {len(Network.orderers)}
        Leader: {Network.leader.id}
        """)
    
    
    @staticmethod
    def initialize_clients():
        for i in range(FabricConfiguration.NO_OF_CLIENTS):
            client = create_client()
            Network.clients[client.id] = client
            
    
    @staticmethod
    def initialize_organizations():
        for i in range(FabricConfiguration.NO_OF_ORGANIZATIONS):
            organization_number = i + 1
            peers = [create_peer() for j in range(FabricConfiguration.NO_OF_PEERS_PER_ORGANIZATION)]
            Network.organizations[str(organization_number)] = peers
            for peer in peers:
                Network.peers[peer.id] = peer
    
    
    @staticmethod
    def initialize_orderers():
        for i in range(FabricConfiguration.NO_OF_ORDERERS):
            orderer = create_orderer()
            Network.orderers[orderer.id] = orderer
            
            
    @staticmethod
    def select_leader():
        Network.leader = random.choice(list(Network.orderers.values()))
        return Network.leader
    
    
def create_client():
    id = generate_id()
    client = Node(id=id)
    return client


def create_peer():
    id = generate_id()
    peer = Peer(id=id)
    return peer


def create_orderer():
    id = generate_id()
    orderer = Orderer(id=id)
    return orderer
        
        
    
    