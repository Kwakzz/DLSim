from datetime import datetime
import random
from Configuration import GeneralConfiguration
from Configuration import coin_based_blockchains
from Util import convert_seconds_to_minutes, get_node_with_blockchain
import matplotlib.pyplot as plt


processed_transaction_counts = []
throughput_values = []
latency_values = []
block_time_values = []
time_values = []


def print_performance_statistics():
    print_throughput()
    print_average_latency()
    print_average_block_time()
    

def record_performance_statistics():
    record_throughput()
    record_latency()
    record_block_time()
    record_no_of_processed_transactions()
    
    
def get_throughput():
    
    random_node = get_node_with_blockchain()
        
    transaction_count = 0
    
    for block in random_node.blockchain:
        transaction_count += block.transaction_count
    
    simulation_time = (GeneralConfiguration.simulation_end_time - GeneralConfiguration.simulation_start_time).total_seconds()
    simulation_time_in_minutes = convert_seconds_to_minutes(simulation_time)
    throughput = transaction_count/simulation_time
    throughput = round(throughput, 2)
    print(f"{transaction_count} transactions processed in {simulation_time_in_minutes} minutes.\n")
    
    return throughput
    
    
def print_throughput():
    throughput = get_throughput()
    print (f"Network throughput: {throughput} transactions/second")
    

def record_throughput():
    throughput_values.append(get_throughput())


def get_average_latency():
    
    random_node = get_node_with_blockchain()
        
    sum_of_latencies = 0
    transaction_count = 0

    for block in random_node.blockchain:
        for transaction in block.transactions.values():
            transaction_count += 1
            latency = (transaction.confirmation_time - transaction.timestamp).total_seconds()
            sum_of_latencies += latency

    if transaction_count == 0:
        return 0  

    average_latency = sum_of_latencies / transaction_count
    average_latency_in_minutes = convert_seconds_to_minutes(average_latency)
    return round(average_latency_in_minutes, 2)
    
    
def print_average_latency():
    latency = get_average_latency()
    print (f"Network average latency is: {latency} minutes.")
    
    
def record_latency():
    latency_values.append(get_average_latency())
    
    
def get_recent_block_time():
    
    random_node = get_node_with_blockchain()
     
    if len(random_node.blockchain) < 2:
        print("Blockchain must contain at least two blocks to calculate average block time.")
        return 0

    recent_block = random_node.blockchain[-1]
    second_recent_block = random_node.blockchain[-2]
    block_time = (recent_block.timestamp - second_recent_block.timestamp).total_seconds()
    block_time_in_minutes = convert_seconds_to_minutes(block_time)
    block_time = round(block_time_in_minutes, 2)
    
    return block_time
    
    
def get_average_block_time():
    
    random_node = get_node_with_blockchain()
            
    no_of_block_times = len(random_node.blockchain) - 1
    cumulative_block_time = 0
    
    if len(random_node.blockchain) < 2:
        print("Blockchain must contain at least two blocks to calculate average block time.")
        return 0
    
    for i in range (0, len(random_node.blockchain)-1):
        first_block = random_node.blockchain[i]
        second_block = random_node.blockchain[i+1]
        block_time = (second_block.timestamp - first_block.timestamp).total_seconds()
        cumulative_block_time += block_time
        
    average_block_time = cumulative_block_time/no_of_block_times
    average_block_time_in_minutes = convert_seconds_to_minutes(average_block_time)
    average_block_time = round(average_block_time_in_minutes, 4)
    return average_block_time
    
    
def print_average_block_time():
    average_block_time = get_average_block_time()
    print(f"Average block time is {average_block_time} minutes")
    
    
def record_block_time():
    block_time_values.append(get_average_block_time())
    
    
def get_no_of_processed_transactions():
    
    random_node = get_node_with_blockchain()
        
    transaction_count = 0
    
    for block in random_node.blockchain:
        transaction_count += block.transaction_count
        
    return transaction_count


def record_no_of_processed_transactions():
    processed_transaction_counts.append(get_no_of_processed_transactions())
    
    
def record_time_values():
    time = (datetime.now() - GeneralConfiguration.simulation_start_time).total_seconds()
    time = convert_seconds_to_minutes(time)
    time_values.append(time)
    
    
def plot_graphs():
    plot_graph_of_throughput_over_time()
    plot_graph_of_latency_over_time()
    plot_graph_of_block_time_over_time()
    plot_processed_transactions_count_over_time()
    
    
def plot_graph_of_throughput_over_time():
    title = "Evolution of Network Throughput"
    x_label = "Time (mins)"
    y_label = "Throughput (tps)"
    plot_graph(time_values, throughput_values, title, x_label, y_label)
    
    
def plot_graph_of_block_time_over_time():
    title = "Evolution of Block Time"
    x_label = "Time (mins)"
    y_label = "Block Time (mins)"
    plot_graph(time_values, block_time_values, title, x_label, y_label)
    
    
def plot_graph_of_latency_over_time():
    title = "Evolution of Latency"
    x_label = "Time (mins)"
    y_label = "Latency (mins)"
    plot_graph(time_values, latency_values, title, x_label, y_label)
    
    
def plot_processed_transactions_count_over_time():
    title = "Processed Transactions Count Over Time"
    x_label = "Time (mins)"
    y_label = "Transaction Count"
    plot_graph(time_values, processed_transaction_counts, title, x_label, y_label)


def plot_graph(x_values, y_values, title, x_label, y_label):
    plt.figure()
    plt.plot(x_values, y_values, color="b", marker="o")
    
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    plt.grid(True)
    plt.show()