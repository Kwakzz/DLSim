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
    
    
    @staticmethod
    def initialize_network():
        Network.initialize_clients()
        Network.initialize_organizations()
        Network.initialize_orderers()
    
    
    @staticmethod
    def initialize_clients():
        for i in range(FabricConfiguration.NO_OF_CLIENTS):
            client = create_client()
            Network.clients[client.id] = client
            
    
    def initialize_organizations():
        for i in range(FabricConfiguration.NO_OF_ORGANIZATIONS):
            organization_number = i+1
            Network.organizations[str(organization_number)] = [create_peer() for j in range(FabricConfiguration.NO_OF_PEERS_PER_ORGANIZATION)]
    
            
    def initialize_orderers():
        for i in range(FabricConfiguration.NO_OF_ORDERERS):
            orderer = create_orderer()
            Network.orderers[orderer.id] = orderer
    
    
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
        
        
    
    