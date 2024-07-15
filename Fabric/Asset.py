from datetime import datetime
from Util import generate_id


class Asset:
    
    def __init__(self, type, owner_id):
        self.id = generate_id()
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
        
    
