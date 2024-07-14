from Fabric.Node import Node as BaseNode
from datetime import datetime


class Orderer (BaseNode):
    
    def __init__(
        self, 
        id,
    ):
        super().__init__ (id)

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
            if orderer == self:
                continue
            else:
                orderer.transactions_log = self.transactions_log
                
                
    def commit_transaction(self, transaction):
        transaction.is_committed = True
                
                
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
        
        transactions_log_copy = list(self.transactions_log.values()) 
        for transaction in transactions_log_copy:
            if cumulative_transaction_size + transaction.size > FabricConfiguration.BLOCK_LIMIT:
                break
            else:
                transaction_batch.append(self.transactions_log.pop(transaction.id))
                cumulative_transaction_size = transaction.size
        
        return transaction_batch
    
    
    def create_block(self):
        
        from Fabric.Block import Block as FabricBlock
        from Fabric.Network import Network as FabricNetwork
        
        block = FabricBlock()
        transaction_batch = self.create_transaction_batch()
        
        for transaction in transaction_batch:
            block.transactions[transaction.id] = transaction
            transaction.confirmation_time = datetime.now()
            
        block.transaction_count = len(block.transactions)
        
        random_peer = next(iter(FabricNetwork.peers.values()))
        block.parent_hash = random_peer.blockchain[-1].hash
        
        block.set_merkle_root()
        block.set_hash()
                
        print(f"{self.id} has created block {block.hash}")
        print(block)
        
        return block
    
    
    def broadcast_block(self, block):
        
        from Fabric.Network import Network as FabricNetwork
        
        for peer in FabricNetwork.peers.values():
            peer.blockchain.append(block)

        
    
def has_leader_received_majority_acknowledgment():
    
    from Fabric.Network import Network as FabricNetwork
    
    no_of_orderers = len(FabricNetwork.orderers)
    acknowledgment_count = 0
    
    for orderer in FabricNetwork.orderers.values():
        
        if orderer.is_log_equal_to_leader_log and orderer is not FabricNetwork.leader:
            acknowledgment_count+=1
    
    print(f"{acknowledgment_count} out of {no_of_orderers-1} orderers have replicated the leader's logs.")
    return is_majority_acknowledgment(acknowledgment_count)

    
def is_majority_acknowledgment(acknowledgment_count):
    
    from Fabric.Network import Network as FabricNetwork
    
    count_of_half_of_orderers = len(FabricNetwork.orderers) // 2
    
    return acknowledgment_count > count_of_half_of_orderers
    
    
def commit_transactions_with_majority_acknowledgment(proposals):
    
    from Fabric.Network import Network as FabricNetwork
    
    for proposal in proposals:
        transaction = proposal.transaction
        FabricNetwork.leader.commit_transaction(transaction)
        
    print("\nTransactions with majority acknowledgment have been committed.")