from datetime import datetime
from time import sleep
from Ethereum.Epoch import Epoch
from Util import print_chain
from Transaction import create_random_transactions


class Slot:
    
    current_slot_number = 0
    block_proposers = {}
    
    
    @staticmethod
    def run_slot ():
        
        from Ethereum.Consensus import Consensus as PoS
        from Ethereum.Consensus import RANDAO      
        from Ethereum.SlashContract import SlashContract
        from Ethereum.Network import Network as EthereumNetwork
                    
        slot_start_time = datetime.now()
        Slot.current_slot_number += 1
        
        formatted_datetime = slot_start_time.strftime("%Y-%m-%d %H:%M:%S")

        print(f"\nEntered Slot {Slot.current_slot_number} at {formatted_datetime}.")
        
        Epoch.update_number()

        PoS.update_validators_list()
        PoS.print_validators()
        
        sleep(2)  
        if Slot.is_new_epoch(): 
            RANDAO.set_random_beacon()
        
        block_proposer = RANDAO.select_block_proposer()
        
        Slot.set_slot_block_proposer(block_proposer, Slot.current_slot_number)
        
        sleep(4)
        block = block_proposer.create_block()
        
        sleep(3)
        block_proposer.broadcast_block(block)
        
        sleep(3)
        is_block_valid = PoS.verify_block(block)
        
        if is_block_valid:
            block.add_to_chain()
            block.finalize_transactions(block_proposer)
            
        else:
            SlashContract.slash(block_proposer)
        
        print(f"Slot {Slot.current_slot_number} completed. Proposer: {block_proposer.id}")
        
        print_chain()
        
        EthereumNetwork.adjust_base_fee(block)
                    
            
    @staticmethod
    def set_slot_block_proposer(block_proposer, slot_number):
        Slot.block_proposers[slot_number] = block_proposer
                        
    
    @staticmethod     
    def get_slot_block_proposer(slot_number):
        return Slot.block_proposers[slot_number]
    
    
    @staticmethod
    def is_new_epoch():
        return Slot.current_slot_number % 32 == 0 or Slot.current_slot_number == 1
    
    
    