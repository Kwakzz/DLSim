import random
from Bitcoin.Node import Node as BitcoinNode
from Ethereum.Node import Node as EthereumNode
from Configuration import BitcoinConfiguration, EthereumConfiguration, SlimcoinConfiguration
from Slimcoin.BurnTransaction import BurnTransaction
from Slimcoin.Block import Block as PoBBlock
from Util import get_chain_length, transaction_propagation_delay
from Bitcoin.Block import genesis_block

class Node (BitcoinNode, EthereumNode):
    
    def __init__(
        self, 
        balance, 
        hashpower,
    ):
        super().__init__(
            balance, 
            hashpower,
        )
        self.blockchain = [genesis_block]
        
    
    def initiate_transaction(self):
        
        from Slimcoin.Transaction import Transaction as SlimcoinTransaction
        from Network import Network
        
        if self.balance > 0:
            transaction_value = random.randrange(1, 5)
            other_nodes = random.sample(list(Network.nodes.values()), len(Network.nodes) - 1)  # Exclude sender
            recipient = random.choice(other_nodes)
            transaction = SlimcoinTransaction(
                sender_id = self.id,
                recipient_id = recipient.id,
                value = transaction_value
            )
            
            transaction.set_hash()
            transaction.set_fee()
            
            # print(transaction)
            return transaction
        
    
    def burn_coins(self, value):
        from Slimcoin.BurnAddress import BurnAddress        
        from Slimcoin.PoB import PoB

        burn_transaction = BurnTransaction(
            value = value,
            sender_id = self.id
        )

        burn_transaction.set_hash()
        
        self.broadcast_transaction(burn_transaction)
        
        BurnAddress.burn_transactions[burn_transaction.id] = burn_transaction
    
        print(burn_transaction)
        # print(f"Burn Hash: {int(burn_transaction.get_burn_hash(), 16)}")
        # print(f"Burn Hash Target: {int(PoB.burn_hash_target, 16)}")
        return burn_transaction
    
    
    def stake(self, amount):
        from Slimcoin.DepositContract import DepositContract

        DepositContract.deposits[self.id] += amount
        print(f"{self.id} has staked {amount} SLM into the deposit contract.")
        return amount
    
    
    def create_pow_block(self):
        from Bitcoin.Block import Block as BitcoinBlock
        
        block = BitcoinBlock()
        cumulative_transaction_size = 0
        
        transactions_memory_pool_copy = list(self.transactions_memory_pool.values())
        for transaction in transactions_memory_pool_copy:
            if cumulative_transaction_size + transaction.size > BitcoinConfiguration.BLOCK_SIZE_LIMIT:
                break
            if transaction.is_valid():
                block.transactions[transaction.id] = transaction
                cumulative_transaction_size += transaction.size
            if transaction.is_burn_transaction():
                transaction.block_index = get_chain_length()
                print(f"Burn transaction {transaction.id} has been deposited in this block.")
    
        block.size=cumulative_transaction_size
        block.transaction_count = len(block.transactions)
        block.height = get_chain_length()
        
        block.parent_hash = self.blockchain[-1].hash
        
        block.set_merkle_root()
        block.set_hash()
        
        self.created_blocks.append(block)
        
        print(block)
        return block
    
    
    def create_pos_block(self):
        from Ethereum.Block import Block as EthereumBlock
        from Slimcoin.Slot import Slot
        
        block = EthereumBlock(slot=Slot.get_current_slot_no())
        cumulative_transaction_gas = 0
        cumulative_transaction_size = 0
        
        transactions_memory_pool_copy = list(self.transactions_memory_pool.values())
        for transaction in transactions_memory_pool_copy:
            if cumulative_transaction_gas + transaction.gas_used > EthereumConfiguration.BLOCK_GAS_LIMIT:
                break
            if transaction.is_valid():
                block.transactions[transaction.id] = transaction
                cumulative_transaction_gas += transaction.gas_used
                cumulative_transaction_size = transaction.size
            if transaction.is_burn_transaction():
                transaction.block_index = get_chain_length()
                print(f"Burn transaction {transaction.id} has been deposited in this block.")
        
        block.gas_used=cumulative_transaction_gas
        block.size = cumulative_transaction_size
        block.height = get_chain_length()
        
        block.transaction_count = len(block.transactions)
        
        block.parent_hash = self.blockchain[-1].hash
        
        block.set_merkle_root()
        block.set_hash()
                
        print(f"{self.id} has created a PoS block with hash, {block.hash}")
        print(block)
        return block
    
    
    def create_pob_block(self, burn_transaction):
        
        block = PoBBlock()    
        cumulative_transaction_size = 0
        
        transactions_memory_pool_copy = list(self.transactions_memory_pool.values())
        for transaction in transactions_memory_pool_copy:
            if cumulative_transaction_size + transaction.size > BitcoinConfiguration.BLOCK_SIZE_LIMIT:
                break
            if transaction.is_valid():
                block.transactions[transaction.id] = transaction
                cumulative_transaction_size += transaction.size
            if transaction.is_burn_transaction():
                transaction.block_index = get_chain_length()
                print(f"Burn transaction {transaction.id} has been deposited in this block.")
        
        block.size=cumulative_transaction_size
        block.transaction_count = len(block.transactions)
        block.height = get_chain_length()
        block.burn_hash = burn_transaction.burn_hash
        
        block.parent_hash = self.blockchain[-1].hash
        
        block.set_merkle_root()
        block.set_hash()
        
        print(f"{self.id} has created a PoB block with hash, {block.hash}.")   
        print(block)
        return block
    
    
    def __str__(self):
        node_type = "Full"
        if not self.blockchain:
            node_type = "Lightweight"
        return f"Node(ID: {self.id}, Balance: {self.balance} SLM, Hashpower: {self.hashpower}, Type: {node_type})\n" 
    
    

def assign_miners():
    
    from Slimcoin.Network import Network as SlimcoinNetwork
    
    no_of_miners = random.choice(SlimcoinConfiguration.no_of_miners)
    SlimcoinConfiguration.miners = random.sample(list(SlimcoinNetwork.nodes.values()), no_of_miners)
            
    for miner in SlimcoinConfiguration.miners:
        print(f"{miner.id} is a miner.")
    print("") 
    
    
def nodes_burn_coins():
    
    from Slimcoin.Network import Network as SlimcoinNetwork
    
    print("\nNodes are burning coins...")
    
    no_of_miners = random.choice(SlimcoinConfiguration.no_of_miners)
    nodes = random.sample(list(SlimcoinNetwork.nodes.values()), no_of_miners)
            
    for node in nodes:
        burn_value = random.randrange(SlimcoinConfiguration.MINIMUM_BURN_VALUE, SlimcoinConfiguration.MAXIMUM_BURN_VALUE)
        node.burn_coins(burn_value)
        
    transaction_propagation_delay()


def nodes_stake():
    from Slimcoin.Network import Network as SlimcoinNetwork
    
    nodes_staking = random.sample(list(SlimcoinNetwork.nodes.values()), 2)
            
    for node in nodes_staking:
        if node.balance > 32:
            amount = random.randrange(EthereumConfiguration.MINIMUM_STAKE, EthereumConfiguration.MAXIMUM_STAKE)
            node.stake(amount)
        else:
            print(f"{node.id} doesn't have enough coins to stake.")   
        
        
def miners_create_pow_blocks():
                
    for miner in SlimcoinConfiguration.miners:
        print(f"{miner.id} is creating a PoW block.")
        miner.create_pow_block()
        
        
