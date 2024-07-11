from datetime import datetime


class Asset:
    
    def __init__(self, id=None, type=None, owner_id=None):
        self.id = id
        self.type = type
        self.owner_id = owner_id
        self.time_created = datetime.now()
        
        
    def __str__(self):
        return f"""
        Asset ( \n
            ID: {self.id},\n
            Type: {self.type},\n
            Owner: {self.owner_id},\n
            Time created: {self.time_created}\n
        )
        """
        
    