from datetime import datetime
from Transaction import Transaction as BaseTransaction

class Transaction (BaseTransaction):
    
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
        )
        self.fee = fee
        
        
    def finalize(self, miner, block):
        
        from Bitcoin.Network import Network as BitcoinNetwork
        from Bitcoin.Consensus import Consensus as PoW
        
        sender = BitcoinNetwork.nodes[self.sender_id]
        recipient = BitcoinNetwork.nodes[self.recipient_id]
        
        self.transfer_funds(sender, recipient)
        PoW.reward_miner(miner, sender, self.fee)
        
        self.confirmation_time = datetime.now()
        
        self.remove_from_memory_pool()
        
        
    def __str__(self):
        fee = round(self.fee, 2)
        return f"""
        Transaction (
            ID: {self.id}, 
            Sender: {self.sender_id}, 
            Recipient: {self.recipient_id}, 
            Timestamp: {self.timestamp}, 
            Value: {self.value} BTC, 
            Size: {self.size} bytes, 
            Fee: {fee} BTC 
        )
        """
    
            
    
    def set_fee(self):
        self.fee = self.size * 0.0005
        self.fee = round(self.fee, 2)
        
        
    def within_sender_balance(self):
        
        from Network import Network
        
        super().within_sender_balance()
        
        sender = Network.nodes[self.sender_id]
        return (self.value + self.fee) <= sender.balance
    