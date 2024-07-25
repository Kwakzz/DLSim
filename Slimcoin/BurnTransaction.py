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
    ):
        super().__init__(
            recipient_id,
            sender_id,
            value,
            fee=0
        )
        self.burn_hash = 0
       
        
    def finalize(self): 
        self.confirmation_time = datetime.now()
        self.remove_from_mempool()
        
    
    def set_internal_hash(self):
        self.id = self.get_internal_hash()
        
        
    def get_burn_hash(self):
        return hex(int(self.get_multiplier() * int(self.id, 16)))
    
    
    def set_burn_hash(self):
        self.burn_hash = self.get_burn_hash()
        
    
    def get_age_in_minutes(self):
        current_time = datetime.now()
        age = (current_time - self.timestamp).total_seconds()
        return convert_seconds_to_minutes(age)
        
    
    def get_multiplier(self):
        return 1 + PoB.decay_rate * self.get_age_in_minutes()
    
        
    def get_effective_burnt_coins(self):
        return self.get_multiplier() * self.value
        
        
    def meets_burn_hash_target(self):
        burn_hash_int = int(self.get_burn_hash(), 16)
        return burn_hash_int < int(PoB.burn_hash_target_in_hex, 16) or burn_hash_int == int(PoB.burn_hash_target_in_hex, 16)
    
    
    def remove_from_mempool(self):
        
        from Slimcoin.Network import Network as SlimcoinNetwork
        
        for node in SlimcoinNetwork.nodes.values():
            node.burn_transactions_memory_pool.pop(self.id)
        
        
    
    
    def __str__(self):
        return f"""
        Burn Transaction (
            Internal Hash: {self.id},
            Multiplier: {self.get_multiplier()}
            Burn Hash: {self.burn_hash}, 
            Burn Address: {burn_address}
            Sender: {self.sender_id}, 
            Timestamp: {self.timestamp}, 
            Value: {self.value} SLM, 
            Size: {self.size} bytes, 
        )
        """
    
