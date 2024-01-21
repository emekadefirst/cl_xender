# File Transfer Project

## Overview

This project provides a simple file transfer mechanism between devices using Python and sockets. It includes a sender script (`sender.py`) for initiating file transfers and a recipient script (`receiver.py`) for receiving files.

## Getting Started

### Prerequisites

- Python (>=3)
- Termux (for Android devices)

### Setup

1. Clone the repository to your local machine.

   ```bash
   git clone https://github.com/emekadefirst/cl_xender.git

2. cd into cl_xender 
   ```bash
   cd cl_xender
4. connect both devices to wifi-hotspot and fetch the ip address
5. replace ip with your actual ip excluding the port, do not termper with the port in the code 
     (("ip-address", 54321)) 
6. do this for both sender and the receiver file

   
7. run
   ```bash
   python main.py
8. on the receiving device type receive bofore typying send on the sending device

Project Structure
main.py: The main script to choose between sending or receiving files.
sender.py: The script to initiate file transfers from a sender device.
receiver.py: The script to receive files on a recipient device.
Troubleshooting
If you encounter any issues, check the IP addresses in the scripts to ensure they match your device's network configuration.
Ensure both devices are on the same network and can reach each other.
Check file paths and names for correctness, especially on the recipient side.

## Credit

Created by:
<a href="https://github.com/emekadefirst" target="_blank"> `[Emeka]` </a>

Minor Contribution by 😁:
<a href="https://github.com/Olayiwolaaa" target="_blank"> `[Olayiwola Karaole]` </a>
