from datetime import datetime
from time import sleep
from Ethereum.Epoch import Epoch
from Util import print_chain


class Slot:
    
    current_slot_number = 0
    slot_thread = None
    block_proposers = {}
    
    
    @staticmethod
    def run_slot ():
        
        from Ethereum.Consensus import Consensus as PoS
        from Ethereum.Consensus import RANDAO        
        
        while True:
            
            slot_start_time = datetime.now()
            Slot.current_slot_number += 1
            
            print(f"\nEntered Slot {Slot.current_slot_number} at {slot_start_time}.")
            
            Epoch.update()

            PoS.update_validators_list()
            PoS.print_validators()
            
            sleep(2)  
            if Slot.is_new_epoch(): 
                RANDAO.set_random_beacon()
            
            block_proposer = RANDAO.select_block_proposer()
            
            Slot.block_proposers[Slot.current_slot_number] = block_proposer
            
            sleep(4)
            print("\nBlock created:")
            block = block_proposer.create_block(slot=Slot.current_slot_number)
            
            sleep(3)
            block_proposer.broadcast_block(block)
            
            sleep(3)
            if PoS.verify_block(block, block_proposer):
                print(f"Attestors have verified block {block.hash}. It has been added to the chain.")
            else:
                print(f"Attestors have detected an invalid block {block.hash}. Proposer {block_proposer.id} will be penalized.")
            
                       
            print(f"Slot {Slot.current_slot_number} completed. Proposer: {Slot.get_block_proposer(Slot.current_slot_number).id}")
            
            print_chain()
                        
    
    @staticmethod     
    def get_block_proposer(slot_number):
        return Slot.block_proposers[slot_number]
    
    
    @staticmethod
    def is_new_epoch():
        return Slot.current_slot_number % 32 == 0 or Slot.current_slot_number == 1
    
    
    