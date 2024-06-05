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
        
        sender.balace -= self.value
        recipient.balance += self.value
        miner.balance += self.fee
        
        
    def __str__(self):
        return f"Transaction (ID: {self.id}, Sender: {self.sender_id}, Recipient: {self.recipient_id}, Timestamp: {self.timestamp}, Value: {self.value} BTC, Size: {self.size} bytes)"
    
            
    
def set_bitcoin_transaction_fee(transaction_size):
    ((transaction_size/1000) * GeneralConfiguration.no_of_pending_transactions) * 0.00005