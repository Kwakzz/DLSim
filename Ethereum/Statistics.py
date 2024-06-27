from Statistics import print_latency, print_throughput, print_average_block_time, record_latency, record_throughput, record_average_block_time

 
def record_ethereum_statistics():
    record_throughput()
    record_latency()
    record_average_block_time()


def print_ethereum_statistics():
    print("\nSTATISTICS:\n")
    print_throughput()
    print_latency()
    print_average_block_time()

    
    

    
    