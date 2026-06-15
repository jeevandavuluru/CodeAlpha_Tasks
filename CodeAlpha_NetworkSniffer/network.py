from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw
from datetime import datetime

# Optional: write logs to a file
LOG_FILE = "sniffer_log.txt"

def log_packet(message):
    """Print to console and write to log file."""
    print(message)
    with open(LOG_FILE, "a") as f:
        f.write(message + "\n")

def process_packet(packet):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if IP in packet:
        ip_layer = packet[IP]
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst
        proto_num = ip_layer.proto

        # Map protocol number to name
        proto_name = "OTHER"
        src_port = dst_port = None

        if TCP in packet:
            proto_name = "TCP"
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
        elif UDP in packet:
            proto_name = "UDP"
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport
        elif ICMP in packet:
            proto_name = "ICMP"

        # Build the log line
        line = f"[{timestamp}] {proto_name} | {src_ip}"
        if src_port:
            line += f":{src_port}"
        line += f" -> {dst_ip}"
        if dst_port:
            line += f":{dst_port}"

        log_packet(line)

        # Show a snippet of the payload if present
        if Raw in packet:
            try:
                payload = bytes(packet[Raw].load)
                snippet = payload[:50]  # first 50 bytes
                log_packet(f"    Payload (first 50 bytes): {snippet}")
            except Exception:
                pass

        log_packet("-" * 70)

def main():
    print("Starting network sniffer... Press Ctrl+C to stop.\n")
    try:
        # count=0 means capture indefinitely; filter can be customized
        sniff(prn=process_packet, store=False, filter="ip")
    except KeyboardInterrupt:
        print("\nSniffer stopped by user.")
    except PermissionError:
        print("Permission denied. Try running this script with admin/root privileges.")

if __name__ == "__main__":
    main()
    