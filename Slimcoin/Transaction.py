from Bitcoin.Transaction import Transaction as BitcoinTransaction

class Transaction (BitcoinTransaction):
    
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
        