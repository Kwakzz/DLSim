from datetime import datetime
from time import sleep
from Util import print_chain
from Configuration import GeneralConfiguration
from Ethereum.Slot import Slot as EthereumSlot

class Slot (EthereumSlot):
    
    
    @staticmethod
    def get_current_slot_no():
        current_slot_number = int((datetime.now() - GeneralConfiguration.simulation_start_time).total_seconds()/12)
        return current_slot_number
    
    
    @staticmethod
    def run_slot ():
        
        from Slimcoin.PoS import Consensus as PoS
        from Slimcoin.PoS import RANDAO      
        from Slimcoin.SlashContract import SlashContract
        from Slimcoin.Network import Network as SlimcoinNetwork
                    
        slot_start_time = datetime.now()
        
        formatted_datetime = slot_start_time.strftime("%Y-%m-%d %H:%M:%S")

        print(f"\nEntered Slot {Slot.current_slot_number} at {formatted_datetime}.")
        
        PoS.update_validators_list()
        PoS.print_validators()
        
        sleep(2)  
        
        block_proposer = RANDAO.select_block_proposer()
        
        if block_proposer is None:
            print(f"No block proposer found in slot {Slot.current_slot_number}.")
        
        else:
            Slot.set_slot_block_proposer(block_proposer, Slot.current_slot_number)
            
            sleep(4)
            block = block_proposer.create_pos_block()
            
            sleep(3)
            block_proposer.broadcast_block(block)
            
            sleep(3)
            is_block_valid = PoS.verify_block(block)
            
            if is_block_valid:
                block.add_to_chain()
                block.finalize_transactions(block_proposer, block)
                
            else:
                SlashContract.slash(block_proposer)
            
            print(f"Slot {Slot.current_slot_number} completed. Proposer: {block_proposer.id}")
        
            print_chain()
            
            SlimcoinNetwork.adjust_base_fee(block)
                    
        
    
    