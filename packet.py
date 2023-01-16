from scapy.all import *
import os
from datetime import datetime
from os import system

# Set a color for each type of packet
colors = {
    "IPv4": "green",
    "ARP": "red",
    "IPv6": "blue"
}
#Set title and message
system('title "Packet Capture - 1 rev B."')
print("Capturing traffic: Active\nClose this console at anytime to end capture, you can view the completed file on your desktop - 'output.html'")

# Create an HTML file to store the output
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
file_path = os.path.join(desktop, "output.html")
with open(file_path, "w") as file:
# Formatting the HTML Document
    file.write("<html>\n<head>\n<script src='https://code.jquery.com/jquery-3.5.1.min.js'></script>\n")
    file.write("<p><b>Key: Protocols are color coded: <span style='color: green'>IPv4 </span><span style='color: red'>ARP </span><span style='color: blue'>IPv6 </span></b></p>")

    file.write("<script>\n")
    file.write("$(document).ready(function() {\n")
    file.write("$('#table').on('keyup', function() {\n")
    file.write("var search = $(this).val().toLowerCase();\n")
    file.write("$('#data tr').filter(function() {\n")
    file.write("$(this).toggle($(this).text().toLowerCase().indexOf(search) > -1)\n")
    file.write("});\n")
    file.write("});\n")
    file.write("});\n")
    file.write("</script>\n")
    file.write("</head>\n")
    file.write("<body>\n")
    file.write("<input type='text' id='table' placeholder='Search..'>\n")
    file.write("<table border='1' id='data'>\n")
    file.write("<tr>\n")
    file.write("<th>Timestamp</th>\n")
    file.write("<th>Source MAC</th>\n")
    file.write("<th>Source IP</th>\n")
    file.write("<th>Destination MAC</th>\n")
    file.write("<th>Destination IP</th>\n")
    file.write("<th>Protocol</th>\n")
    file.write("</tr>\n")

#Defining Network Traffic Packets
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
#Writing to html table and formatting
        file.write("<tr><td>" + str(datetime.now()) + "</td><td style='color: " + colors.get(protocol, "black") + "'>" + src_mac + "</td><td>" + src_ip + "</td><td>" + dst_mac + "</td><td>" + dst_ip + "</td><td>" + protocol + "</td></tr>\n")

    sniff(prn=packet_info)
    file.write("</table>\n</body>\n</html>")
