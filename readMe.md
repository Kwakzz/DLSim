# DLSim: A Configurable Blockchain Simulator

## Overview
DLSim is a configurable blockchain simulator designed to model and analyze the performance of various blockchain platforms, including Bitcoin, Ethereum, Hyperledger Fabric, and Slimcoin. This simulator allows users to experiment with different network configurations and consensus mechanisms, providing valuable insights into performance.

## Features
- **Modular Design**: Easily extendable to include additional blockchain platforms and consensus algorithms.
- **Configurable Parameters**: Adjust parameters such as the number of nodes, block size, block interval, and transaction volume.
- **Comparative Analysis**: Empirically compare the performance of different blockchain platforms.
- **User-Friendly Interface**: Intuitive interface for configuring simulations and visualizing results.

## Installation
To install and run DLSim, follow these steps:

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/Kwakzz/DLSim.git
   cd DLSim
   python Main.py

## Usage
1. Configure parameters in Configuration.py. We recommend you only change the following:
- **no_of_rounds**
- **no_of_nodes**
- **INITIAL_DIFFICULTY_TARGET_HEX**
2. Set number of desired blocks by editing the no_of_rounds variable in GeneralConfiguration.
3. Use selected_platform variable in GeneralConfiguration to switch platforms. 
4. Run python Main.py while in the root directory

## Authors
DLSim was developed by Kwaku Osafo and Laura Larbi-Tieku as part of their capstone project at Ashesi University. For any questions or contributions, please contact:

- Kwaku Osafo: kwakuosafo20@gmail.com
- Laura Larbi-Tieku: lauralarbi02@gmail.com
