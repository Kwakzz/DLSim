from datetime import datetime
from hashlib import sha256
from Configuration import SlimcoinConfiguration
from Slimcoin.Transaction import Transaction as SlimcoinTransaction
from Slimcoin.PoB import PoB
from Util import convert_seconds_to_minutes, get_last_block, get_node_with_blockchain, get_blockchain
from Slimcoin.BurnAddress import BurnAddress


class BurnTransaction(SlimcoinTransaction):
    
    def __init__(
        self, 
        sender_id,
        value,
        recipient_id = BurnAddress.address,
        fee=0,
    ):
        super().__init__(
            recipient_id,
            sender_id,
            value,
            fee=0
        )
        self.internal_hash = 0
        self.burn_hash = 0
        self.block_index = 0
       
        
    def finalize(self, block_proposer, block): 
        from Slimcoin.Network import Network as SlimcoinNetwork

        sender = SlimcoinNetwork.nodes[self.sender_id]
        sender.balance -= self.value
        self.confirmation_time = datetime.now()
        self.remove_from_memory_pool()
                
    
    def is_valid(self):
        return self.is_burn_transaction and self.within_sender_balance
        
        
    def get_multiplier(self):        
        min_pow_blocks = SlimcoinConfiguration.MINIMUM_NUMBER_OF_POW_BLOCKS_PRECEEDING_POB_BLOCK
        blocks_since_last_pob_block = get_last_block().height - self.block_index
        burn_constant = SlimcoinConfiguration.BURN_CONSTANT
        number_of_coins_burned = self.value
        burn_hash_double = SlimcoinConfiguration.BURN_HASH_DOUBLE
        
        if min_pow_blocks > blocks_since_last_pob_block:
            return 0
        
        multiplier = (burn_constant/number_of_coins_burned) * 2 **((blocks_since_last_pob_block - min_pow_blocks)/burn_hash_double)
        
        return multiplier
    
    
    def get_internal_hash(self):
        from Util import sha256_hash
        transaction_block_hash = get_blockchain()[self.block_index].hash
        most_recent_block_hash = get_blockchain()[-1].hash
        
        transaction_block_hash_bytes = bytes.fromhex(transaction_block_hash)
        transaction_id_bytes = bytes.fromhex(self.id)
        most_recent_block_hash_bytes = bytes.fromhex(most_recent_block_hash)
        
        data = transaction_block_hash_bytes + transaction_id_bytes + most_recent_block_hash_bytes
        
        internal_hash = sha256_hash(data)
        
        return internal_hash
        
    
    def set_internal_hash(self):
        self.internal_hash = self.get_internal_hash()
        
        
    def get_burn_hash(self):
        # return hex(int(self.get_multiplier() * int(self.get_internal_hash(), 16)))
        burn_hash = hex(int(self.get_multiplier() * int(self.get_internal_hash(), 16)))
        burn_hash = burn_hash.rstrip('0').rstrip('x')
        if not burn_hash.startswith('0x'):
            burn_hash = '0x' + burn_hash
        return burn_hash
    
    
    def set_burn_hash(self):
        self.burn_hash = self.get_burn_hash()
    
        
    def get_effective_burnt_coins(self):
        return self.get_multiplier() * self.value
        
        
    def meets_burn_hash_target(self):
        self.set_internal_hash()
        self.set_burn_hash()
        burn_hash_int = int(self.get_burn_hash(), 16)
        if burn_hash_int < int(PoB.burn_hash_target_in_hex, 16) or burn_hash_int == int(PoB.burn_hash_target_in_hex, 16):
            print(f"\nBurn transaction {self.id}'s burn hash {self.burn_hash} meets the burn hash target.")
            print(self)
            print()
            return True
        return False
        
    
    def __str__(self):
        return f"""
        Burn Transaction (
            ID: {self.id},
            Internal Hash: {self.internal_hash},
            Multiplier: {self.get_multiplier()}
            Burn Hash: {self.burn_hash}, 
            Burn Address: {BurnAddress.address}
            Sender: {self.sender_id}, 
            Timestamp: {self.timestamp}, 
            Value: {self.value} SLM, 
            Size: {self.size} bytes, 
        )
        """
    
