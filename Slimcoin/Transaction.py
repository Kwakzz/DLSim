from datetime import datetime
from Bitcoin.Transaction import Transaction as BitcoinTransaction
from Ethereum.Transaction import Transaction as EthereumTransaction
from Slimcoin.Network import Network as SlimcoinNetwork

class Transaction (BitcoinTransaction, EthereumTransaction):
    
    def __init__(
        self, 
        recipient_id,
        sender_id,
        value,
        fee=0,
    ):
        super().__init__(
            recipient_id,
            sender_id,
            value,
            fee=0
        )
        
        
    def finalize(self, block_creator, block):
        
        from Slimcoin.PoS import PoS as PoS
        from Bitcoin.Consensus import Consensus as PoW
        
        sender = SlimcoinNetwork.nodes[self.sender_id]
        recipient = SlimcoinNetwork.nodes[self.recipient_id]
        
        self.transfer_funds(sender, recipient)
        
        if block.is_pos_block():
            PoS.reward_validator(block_creator, sender, self.tip)
        else:
            PoW.reward_miner(block_creator, sender, self.fee)
        
        self.confirmation_time = datetime.now()
        
        self.remove_from_memory_pool()
    
        
    def is_burn_transaction(self):
        from Slimcoin.BurnAddress import BurnAddress
        return self.recipient_id == BurnAddress.address
    
        
    def __str__(self):
        fee = round(self.fee, 2)
        return f"""
        Transaction (
            ID: {self.id}, 
            Sender: {self.sender_id}, 
            Recipient: {self.recipient_id}, 
            Timestamp: {self.timestamp}, 
            Value: {self.value} SLM, 
            Size: {self.size} bytes, 
            Fee: {fee} SLM 
        )
        """