from datetime import datetime
from hashlib import sha256
from Configuration import SlimcoinConfiguration
from Slimcoin.Transaction import Transaction as SlimcoinTransaction
from Slimcoin.Consensus import Consensus as PoB
from Util import convert_seconds_to_minutes, generate_id


burn_address = generate_id()


class BurnTransaction(SlimcoinTransaction):
    
    def __init__(
        self, 
        sender_id,
        value,
        recipient_id = burn_address,
        fee=0,
        multiplier = 0
    ):
        super().__init__(
            recipient_id,
            sender_id,
            value,
            fee=0
        )
        self.multiplier = multiplier
        self.effective_power = 0
    
    
    def set_internal_hash(self):
        self.id = self.get_internal_hash()
        
        
    def get_burn_hash(self):
        return hex(int(self.multiplier * int(self.id, 16)))

    
    
    def get_age_in_minutes(self):
        current_time = datetime.now()
        age = (current_time - self.timestamp).total_seconds()
        return convert_seconds_to_minutes(age)
        
    
    def get_multiplier(self):
        return 1 + PoB.decay_rate * self.get_age_in_minutes()
        
    
    def set_multiplier(self):
        self.multiplier = self.get_multiplier()
        
        
    def meets_burn_hash_target(self):
        burn_hash_int = int(self.get_burn_hash())
        return burn_hash_int < int(SlimcoinConfiguration.current_burn_hash_target) or burn_hash_int == SlimcoinConfiguration.current_burn_hash_target
    
    
    def is_valid(self):
        return self.recipient_id == burn_address
    
    
    def __str__(self):
        return f"""
        Burn Transaction (
            Internal Hash: {self.id},
            Multiplier: {self.multiplier}
            Burn Hash: {self.get_burn_hash()}, 
            Burn Address: {burn_address}
            Sender: {self.sender_id}, 
            Timestamp: {self.timestamp}, 
            Value: {self.value} SLM, 
            Size: {self.size} bytes, 
        )
        """
    
