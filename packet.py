import os
import datetime
from scapy.all import *

# create a new file on the desktop
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 
file_name = "sniffed_packets.txt"
file_path = os.path.join(desktop, file_name)
with open(file_path, "w") as f:
    f.write("Sniffed packets:\n\n")

stop_sniffing = False

def handle_pause_resume(packet):
    global stop_sniffing
    if stop_sniffing:
        return
    packet_str = "Timestamp: {}\nSource MAC: {}\nDestination MAC: {}\nSource IP: {}\nDestination IP: {}\nPacket size: {}\nProtocol: {}\n\n".format(datetime.datetime.now(), packet[Ether].src, packet[Ether].dst, packet[IP].src, packet[IP].dst, packet[IP].len, packet[IP].proto)
    with open(file_path, "a") as f:
        f.write(packet_str)
    print(packet_str)
    
def start_sniffing():
    global stop_sniffing
    stop_sniffing = False
    sniff(prn=handle_pause_resume, filter="ip", store=0)
    
def stop_sniffing():
    global stop_sniffing
    stop_sniffing = True

# start sniffing
start_sniffing()

# code to handle pause and resume
while True:
        user_input = input("Enter 'p' to pause, 'r' to resume, 'q' to quit: ")

