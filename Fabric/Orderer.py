from time import sleep
from Fabric.Node import Node as BaseNode
from datetime import datetime


class Orderer (BaseNode):
    
    def __init__(
        self, 
        id,
    ):
        super().__init__ (id)
        self.transactions_log = []

    def __str__(self):
        return f"""
        Orderer {self.id}
        """
        
        
    def append_entries(self): 
        """ 
        Replicate transaction log in other orderer nodes. This function is executed by the leader
        """
        
        from Fabric.Network import Network as FabricNetwork
        
        for orderer in FabricNetwork.orderers.values():
            if orderer is not self:
                orderer.transactions_log = self.transactions_log
                
                
    def print_transactions_log(self):
        
        print(f"\n{self.id}'s Transactions Log:")
        for transaction in self.transactions_log:
            print(transaction)
        print()
                
                
    def is_log_equal_to_leader_log(self):
        
        from Fabric.Network import Network as FabricNetwork
        
        if self.transactions_log == FabricNetwork.leader.transactions_log:
            return True
        
        
    def create_transaction_batch(self):
        
        from Configuration import FabricConfiguration
        
        transaction_batch = []
        
        cumulative_transaction_size = 0
        
        transactions_log_copy = self.transactions_log
        
        sleep(FabricConfiguration.BATCH_TIMEOUT)
         
        for transaction in transactions_log_copy:
            if (cumulative_transaction_size + transaction.size > FabricConfiguration.PREFFERED_MAX_BYTES) or (len(transaction_batch) == FabricConfiguration.MAX_TRANSACTION_COUNT_PER_BLOCK):
                break
            else:
                transaction_batch.append(transaction)
                self.transactions_log.remove(transaction)
                cumulative_transaction_size = transaction.size
        
        return transaction_batch
    
    
    def create_block(self):
        
        from Fabric.Block import Block as FabricBlock
        from Fabric.Network import Network as FabricNetwork
        from Configuration import FabricConfiguration
        
        block = FabricBlock(
            sequence_number=FabricConfiguration.block_sequence_number
        )
        FabricConfiguration.block_sequence_number += 1
        transaction_batch = self.create_transaction_batch()
        
        for transaction in transaction_batch:
            block.transactions[transaction.id] = transaction
            block.size += transaction.size
            transaction.confirmation_time = datetime.now()
            
        block.transaction_count = len(block.transactions)
        
        random_peer = next(iter(FabricNetwork.peers.values()))
        block.parent_hash = random_peer.blockchain[-1].hash
        
        block.set_merkle_root()
        block.set_hash()
                
        print(f"\n{self.id} has created block {block.hash}")
        print(block)
        
        return block
    
    
    def broadcast_block_to_peers(self, block):
        
        from Fabric.Network import Network as FabricNetwork
        
        for peer in FabricNetwork.peers.values():
            peer.blockchain.append(block)