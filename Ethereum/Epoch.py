class Epoch:
    
    current_epoch = 1
    
    @staticmethod
    def update():
        
        from Ethereum.Slot import Slot
        
        if Slot.current_slot_number % 32 == 0:
            Epoch.current_epoch += 1