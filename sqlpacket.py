import sqlite3
from scapy.all import *

# Create a new SQLite database
try:
    conn = sqlite3.connect('packets.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name from sqlite_master WHERE type='table' AND name='packets'")
    if cursor.fetchone():
        print("Table already exists. Writing to existing table")
    else:
        cursor.execute("CREATE TABLE packets (timestamp TEXT, src_ip TEXT, src_mac TEXT, src_port INTEGER, dst_ip TEXT, dst_mac TEXT, dst_port INTEGER, protocol TEXT)")
        print("Table does not exist. Creating new table")
except sqlite3.Error as e:
    print(f"An error occurred while connecting to the database: {e}")

def packet_callback(packet):
    timestamp = packet.time
    if packet.haslayer(Ether):
        src_mac = packet[Ether].src
        dst_mac = packet[Ether].dst
    else:
        src_mac = "NA"
        dst_mac = "NA"

    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto
    else:
        src_ip = "NA"
        dst_ip = "NA"
        protocol = "NA"
    if packet.haslayer(TCP) or packet.haslayer(UDP):
        if packet.haslayer(TCP):
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
        else:
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport
    else:
        src_port = "NA"
        dst_port = "NA"
    try:
        # Insert packet information into the existing table 
        cursor.execute("INSERT INTO packets (timestamp, src_ip, src_mac, src_port, dst_ip, dst_mac, dst_port, protocol) VALUES (?,?,?,?,?,?,?,?)", (timestamp, src_ip, src_mac, src_port, dst_ip, dst_mac, dst_port, protocol))
        conn.commit()
    except sqlite3.Error as e:
        print(f"An error occurred while inserting into the database: {e}")

# Use Scapy to capture packets
try:
    sniff(prn=packet_callback, store=0)
except Exception as e:
    print(f"An error occurred while capturing packets: {e}")

# Close the database connection
try:
    cursor.close()
    conn.close()
except sqlite3.Error as e:
    print(f"An error occurred while closing the database connection: {e}")
