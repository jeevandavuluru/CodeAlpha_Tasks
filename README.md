# CodeAlpha_NetworkSniffer

## 📌 Project Overview
This project is a **Basic Network Sniffer** built using Python and the `scapy` library, developed as part of the **CodeAlpha Cyber Security Internship — Task 1**.

The program captures live network packets passing through the system's network interface, analyzes their structure, and displays useful information such as source/destination IP addresses, transport protocol (TCP/UDP/ICMP), port numbers, and a snippet of the packet payload.

This project helps in understanding:
- How data flows through a network
- The structure of network packets (IP, TCP, UDP, ICMP layers)
- The basics of network protocols
- How tools like Wireshark work under the hood

---

## ⚙️ Features
- Captures live network traffic in real time
- Identifies and displays:
  - Timestamp of each packet
  - Source and Destination IP addresses
  - Protocol type (TCP / UDP / ICMP)
  - Source and Destination ports (for TCP/UDP)
  - First 50 bytes of payload data (if present)
- Logs all captured packet details to `sniffer_log.txt` for later review



## ▶️ How to Run

While the script is running, generate some traffic (e.g., open a browser, visit a website, or run `ping google.com`) to see captured packets in real time.

Press `Ctrl + C` to stop the sniffer.

---

## 📄 Output
- Captured packet details are displayed in the console.
- All details are also saved to `sniffer_log.txt` in the same directory.

### Sample Output
```
[2026-06-15 10:32:11] TCP | 192.168.1.5:54231 -> 142.250.182.106:443
    Payload (first 50 bytes): b'\x17\x03\x03\x00\x2a...'
----------------------------------------------------------------------
[2026-06-15 10:32:12] UDP | 192.168.1.5:5353 -> 224.0.0.251:5353
----------------------------------------------------------------------
[2026-06-15 10:32:13] ICMP | 192.168.1.5 -> 8.8.8.8
----------------------------------------------------------------------
```

