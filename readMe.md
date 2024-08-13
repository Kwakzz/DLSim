# DLSim: A Configurable Blockchain Simulator

## Overview

DLSim is a configurable blockchain simulator designed to model and analyze the performance of various blockchain platforms, including Bitcoin, Ethereum, Hyperledger Fabric, and Slimcoin. This simulator allows users to experiment with different network configurations and consensus mechanisms, providing valuable insights into performance.

## Features

- **Object-Oriented:** Elements in a blockchain platform are represented as objects.
- **Extensive:** Models four blockchain platforms: Bitcoin, Ethereum, Hyperledger Fabric, and Slimcoin.
- **Modular Design:** Platforms are separated into folders, with each containing derived and exclusive classes.
- **Configurable Parameters:** Parameters such as the number of nodes, block size, transaction volume, etc., can be adjusted. However, we recommend you adjust only variables in `Configuration.py`, and not constants.
- **Performance Statistics:** Records the average throughput, latency, and block time of a platform at the end of every simulation round.
- **Consensus Algorithms:** The consensus mechanisms of Bitcoin, Ethereum, Hyperledger Fabric, and Slimcoin are modeled. For example, in the Bitcoin simulation, the PoW Consensus mechanism is modeled. When “Nodes A, B, and C are mining…” is printed to the terminal, these node objects are computing hashes simultaneously, in search of one that meets the difficulty target.
- **Terminal Interface:** Simulation flow and performance statistics are logged in the terminal.

## Installation

To install and run DLSim, follow these steps:

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/Kwakzz/DLSim.git
    cd DLSim
    pip freeze > requirements.txt
    pip install -r requirements.txt 
    python Main.py
    ```

## Usage

1. **Configure parameters in `Configuration.py`.** We recommend you only change the following:

    - `no_of_rounds`
    - `no_of_nodes`
    - `INITIAL_DIFFICULTY_TARGET_HEX`
    
    Refer to Hyperledger Fabric's documentation for appropriate Fabric configurations. All constants in the configuration classes are based on real-world settings.
    
2. **Set the number of desired blocks** by editing the `no_of_rounds` variable in `GeneralConfiguration`. For Ethereum, edit the `max_no_of_slots` variable in the `EthereumConfiguration` class.

3. **Use the `selected_platform` variable** in `GeneralConfiguration` to switch platforms.

4. **Run** `python Main.py` **while in the root directory.**

## Authors

DLSim was developed by Kwaku Osafo and Laura Larbi-Tieku as part of their capstone project at Ashesi University. For any questions or contributions, please contact:

- **Kwaku Osafo:** [kwakuosafo20@gmail.com](mailto:kwakuosafo20@gmail.com)
- **Laura Larbi-Tieku:** [lauralarbi02@gmail.com](mailto:lauralarbi02@gmail.com)
