from scapy.all import *
import os
from datetime import datetime

# Set a color for each type of packet
colors = {
    "IPv4": "green",
    "ARP": "red",
    "IPv6": "blue"
}

# Create an HTML file to store the output
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
file_path = os.path.join(desktop, "output.html")
with open(file_path, "w") as file:
    file.write("<html>\n<head>\n")
    file.write("<style>\n")
    file.write("table, th, td {\n")
    file.write("border: 1px solid black;\n")
    file.write("border-collapse: collapse;\n")
    file.write("padding: 5px;\n")
    file.write("}\n")
    file.write("th {\n")
    file.write("background-color: lightgray;\n")
    file.write("}\n")
    file.write("</style>\n")
    file.write("</head>\n<body>\n")
    file.write("<table>\n")
    file.write("<tr><th>Timestamp</th><th>Source MAC</th><th>Source IP</th><th>Destination MAC</th><th>Destination IP</th><th>Protocol</th></tr>\n")
    def packet_info(packet):
        src_mac = packet[Ether].src
        dst_mac = packet[Ether].dst
        if packet.haslayer(IP):
            protocol = "IPv4"
            src_ip = packet[IP].src
            dst_ip = packet[IP].dst
        elif packet.haslayer(ARP):
            protocol = "ARP"
            src_ip = packet[ARP].psrc
            dst_ip = packet[ARP].pdst
        elif packet.haslayer(IPv6):
            protocol = "IPv6"
            src_ip = packet[IPv6].src
            dst_ip = packet[IPv6].dst
        else:
            src_ip = "Unknown"
            dst_ip = "Unknown"
            protocol = "Unknown"

        file.write("<tr><td>" + str(datetime.now()) + "</td><td style='color: " + colors.get(protocol, "black") + "'>" + src_mac + "</td><td>" + src_ip + "</td><td>" + dst_mac + "</td><td>" + dst_ip + "</td><td>" + protocol + "</td></tr>\n")

    sniff(prn=packet_info)
    file.write("</table>\n</body>\n</html>")
