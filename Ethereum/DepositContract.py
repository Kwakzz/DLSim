from itertools import combinations
import random
from Ethereum.Network import Network as EthereumNetwork
from Configuration import EthereumConfiguration

class DepositContract:
    
    deposits = {}
    events = []
    
    
    @staticmethod
    def create():       
        for node in EthereumNetwork.nodes.values():
            DepositContract.deposits[node.id] = 0
        event = f"Deposit Contract created."
        DepositContract.events.append(event)
        print(event)
        
    
    @staticmethod   
    def print_deposits():
        print("\nDeposits")
        for deposit in DepositContract.deposits.items():
            if deposit[1] != 0:
                print(f"Node {deposit[0]}: {deposit[1]} ETH")
            
            
    @staticmethod
    def get_total_stake():
        return sum(DepositContract.deposits.values())
    
        
        
    @staticmethod
    def deposit(node, amount):
        if node.balance >= amount:
            node.balance -= amount
            DepositContract.deposits[node.id] += amount
            event = f"Node {node.id} deposited {amount} ETH. New deposit: {DepositContract.deposits[node.id]} ETH"         
        else:
            event = f"Node {node.id} does not have enough balance to deposit {amount} ETH"
            
        DepositContract.events.append(event)
        print(event)
        
        
    @staticmethod
    def withdraw(node, amount):
        if DepositContract.deposits[node.id] >= amount:
            DepositContract.deposits[node.id] -= amount
            node.balance += amount
            event = f"Node {node.id} withdrew {amount} ETH. New deposit: {DepositContract.deposits[node.id]} ETH"
        else:
            event = f"Node {node.id} does not have enough deposit to withdraw {amount} ETH"

        DepositContract.events.append(event)
        print(event)
        
        
    @staticmethod
    def print_events():
        print("\nDeposit Contract Events")
        for event in DepositContract.events:
            print(event)
        
        
def nodes_stake():
    
    nodes_staking = random.choice(list(combinations(EthereumNetwork.nodes.values(), 2)))
            
    for node in nodes_staking:
        if node.balance > 32:
            amount = random.randrange(EthereumConfiguration.MINIMUM_STAKE, EthereumConfiguration.MAXIMUM_STAKE)
            node.stake(amount)
        else:
            print(f"{node.id} doesn't have enough coins to stake.")   