import hashlib


def sha256_hash(data):    
    if isinstance(data, str):
        data = data.encode('utf-8')
    return hashlib.sha256(data).hexdigest()
                
       
def double_256_hash(data):
    if isinstance(data, str):
        data = data.encode('utf-8')
        
    return hashlib.sha256(hashlib.sha256(data).digest()).hexdigest()
         
            
def print_chain():
    
    from Network import Network
    
    random_node = next(iter(Network.nodes.values()))
    
    print ("Blockchain:", end=" ")
    
    print ("[", end="")
    for block in random_node.blockchain:
        print(block.hash, end="->")
    print("]")
    
    
def convert_seconds_to_minutes(time):
    return round(time/60, 2)


def convert_bytes_to_megabytes(size):
    return size/2**20


# Convert to %Y-%m-%d %H:%M:%S  
def format_datetime(datetime):
    return datetime.strftime("%Y-%m-%d %H:%M:%S")