# Task 1: Basic Network Sniffer

## Objective
The objective of this task is to understand how network packets flow through a system and how packet sniffing works at the IP and transport layer level.

---

## Description
In this task, I implemented a **basic network sniffer** using Python and the Scapy library.  
The program captures live network traffic and displays important packet details such as IP addresses, ports, and protocols.

The sniffer operates in **passive mode**, meaning it only observes packets and does not send or modify any network traffic.

---

## Features Implemented
- Captures live network packets
- Filters and processes only IP packets
- Identifies TCP and UDP protocols
- Displays:
  - Source IP address
  - Destination IP address
  - Source and destination ports
  - Protocol type
- Captures a limited number of packets (`count = 10`) for controlled observation

---

## How It Works
- Scapy’s `sniff()` function is used to capture packets.
- A callback function processes each captured packet.
- The program checks whether the packet contains an IP layer.
- If TCP or UDP layers are present, port numbers are extracted.
- Only packets generated **after the program starts running** are captured.

---

## Tools Used
- Python 3
- Scapy
- Npcap (required on Windows for packet capturing)

---

## How to Run
1. Install Scapy:
   ```bash
   pip install scapy

