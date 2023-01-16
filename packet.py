from scapy.all import *
import os
from datetime import datetime

# Set a color for each type of packet
colors = {
    "IPv4": "green",
    "ARP": "red",
    "IPv6": "blue"
}
#Set title and message
system('title "Packet Capture - 1 rev A."')
print("Capturing traffic: Active\nClose this console at anytime to end capture, you can view the completed file on your desktop - 'output.html'")

# Create an HTML file to store the output
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
file_path = os.path.join(desktop, "output.html")
with open(file_path, "w") as file:
# Formatting the HTML Document
# Javascript for the filter ability
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
    file.write("<script>\n")
    file.write("function filterTable() {\n")
    file.write("    // Declare variables\n")
    file.write("    var input, filter, table, tr, td, i, txtValue;\n")
    file.write("    input = document.getElementById('filterInput');\n")
    file.write("    filter = input.value.toUpperCase();\n")
    file.write("    table = document.getElementById('table');\n")
    file.write("    tr = table.getElementsByTagName('tr');\n")
    file.write("    \n")
    file.write("    // Loop through all table rows, and hide those who don't match the search query\n")
    file.write("    for (i = 0; i < tr.length; i++) {\n")
    file.write("        td = tr[i].getElementsByTagName('td')[2];\n")
    file.write("        if (td) {\n")
    file.write("            txtValue = td.textContent || td.innerText;\n")
    file.write("            if (txtValue.toUpperCase().indexOf(filter) > -1) {\n")
    file.write(" tr[i].style.display = '';\n")
    file.write(" } else {\n")
    file.write(" tr[i].style.display = 'none';\n")
    file.write(" }\n")
    file.write(" }\n")
    file.write(" }\n")
    file.write("}\n")
    file.write("</script>\n")
    file.write("</head>\n<body>\n")
    file.write("<p>Key: <span style='color: green'>IPv4</span>, <span style='color: red'>ARP</span>, <span style='color: blue'>IPv6</span></p>")
    file.write("<input type='text' id='filterInput' onkeyup='filterTable()' placeholder='Search for IP address...'>")
    file.write("<table id='table'>\n")
    file.write("<tr><th>Timestamp</th><th>Source MAC</th><th>Source IP</th> <th>Destination MAC</th><th>Destination IP</th><th>Protocol</th></tr>\n")
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
