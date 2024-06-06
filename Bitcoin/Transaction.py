from Configuration import GeneralConfiguration
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
        
        
    def finalize(self, miner):
        
        from Network import Network
        
        miner = Network.nodes[miner.id]
        sender = Network.nodes[self.sender_id]
        recipient = Network.nodes[self.recipient_id]
        
        sender.balance -= self.value
        sender.balance -= self.fee
        recipient.balance += self.value
        miner.balance += self.fee
        
        
    def __str__(self):
        return f"Transaction (ID: {self.id}, Sender: {self.sender_id}, Recipient: {self.recipient_id}, Timestamp: {self.timestamp}, Value: {self.value} BTC, Size: {self.size} bytes, Fee: {self.fee} BTC)"
    
            
    
    def set_fee(self):
        self.fee = self.size * 0.0005
        
        
    def within_sender_balance(self):
        
        from Network import Network
        
        super().within_sender_balance()
        
        sender = Network.nodes[self.sender_id]
        return (self.value + self.fee) <= sender.balance
    