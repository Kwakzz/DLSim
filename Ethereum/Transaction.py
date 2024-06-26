import random
from Configuration import EthereumConfiguration, GeneralConfiguration
from Transaction import Transaction as BaseTransaction

class Transaction (BaseTransaction):
    
    def __init__(self, recipient_id, sender_id, value, id=0):
        super().__init__(recipient_id, sender_id, value, id=0)
        self.max_fee_per_gas = suggest_max_fee_per_gas()
        self.tip = suggest_tip() * 10**-9 # 1 gwei = 1*10^-9 ETH
        self.gas_used = EthereumConfiguration.transaction_gas
        
        
    def get_effective_gas_price(self):
        return self.tip + EthereumConfiguration.current_base_fee
    
    
    def get_transaction_fee(self):
        return self.get_effective_gas_price() * self.gas_used
    
    
    def get_refund(self):
        excess = self.max_fee_per_gas - self.get_effective_gas_price()
        return excess * self.gas_used
    
    
    def finalize(self, block_proposer):
        
        from Ethereum.Network import Network as EthereumNetwork
        from Ethereum.Consensus import Consensus as PoS
        
        sender = EthereumNetwork.nodes[self.sender_id]
        recipient = EthereumNetwork.nodes[self.recipient_id]
        
        self.transfer_funds(sender, recipient)
        PoS.reward_validator(block_proposer, sender, self.tip)
        
        for node in EthereumNetwork.nodes.values():
            node.transactions_memory_pool.pop(self.id)
    
    
    def __str__(self):
        return f"Transaction (ID: {self.id}, Sender: {self.sender_id}, Recipient: {self.recipient_id}, Timestamp: {self.timestamp}, Value: {self.value} BTC, Size: {self.size} bytes, Gas Used: {self.gas_used}, Fee: {convert_eth_to_gwei(self.get_transaction_fee())} gwei)"
         
    
def suggest_max_fee_per_gas():
    return (EthereumConfiguration.max_tip* (10**-9)) + EthereumConfiguration.current_base_fee


def suggest_tip():
    return random.randrange(1, EthereumConfiguration.max_tip)


def convert_eth_to_gwei(fee):
    gwei_amount = fee * 10**9
    return round(gwei_amount, 2)