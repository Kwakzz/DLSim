import random
from Ethereum.Block import genesis_block
from Bitcoin.Node import Node as BitcoinNode
from Slimcoin import BurnTransaction

class Node (BitcoinNode):
    
    def __init__(
        self, 
        balance, 
        hashpower,
    ):
        super().__init__(
            balance, 
            hashpower,
        )
        
    
    def burn_coins(self, value):
        burn_transaction = BurnTransaction(
            value = value,
            sender_id = self.id
        )

        burn_transaction.set_internal_hash()
        burn_transaction.set_multiplier()
        self.balance -= value
        
        self.broadcast_transaction_without_delay(burn_transaction)
        
        print(f"{value} SLM have been burnt. Burn transaction {self.id} has been broadcasted to the network.")
        return burn_transaction
    
    
    def __str__(self):
        return BitcoinNode.__str__(self)
    