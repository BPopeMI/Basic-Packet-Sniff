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
    # Javascript for the filter ability
    file.write("<script>\n")
    file.write("function filterTable() {\n")
    file.write("    var filter = document.getElementById('filterInput').value.toUpperCase();\n")
    file.write("    var table = document.getElementById('table');\n")
    file.write("    var tr = table.getElementsByTagName('tr');\n")
    file.write("    for (i = 0; i < tr.length; i++) {\n")
    file.write("        var td1 = tr[i].getElementsByTagName('td')[1];\n")
    file.write("        var td4 = tr[i].getElementsByTagName('td')[4];\n")
    file.write("        var td6 = tr[i].getElementsByTagName('td')[6];\n")
    file.write("        var th = tr[i].getElementsByTagName('th')[0];\n")
    file.write("        if (th) {\n")
    file.write("            var txtValueTh = th.textContent || th.innerText;\n")
    file.write("            if (txtValueTh.toUpperCase().indexOf(filter) > -1) {\n")
    file.write("                tr[i].style.display = 'table-row';\n")
    file.write("                continue;\n")
    file.write("            }\n")
    file.write("        }\n")
    file.write("        if (td1) {\n")
    file.write("            var txtValue1 = td1.textContent || td1.innerText;\n")
    file.write("            if (txtValue1.toUpperCase().indexOf(filter) > -1) {\n")
    file.write("                tr[i].style.display = '';\n")
    file.write("                continue;\n")
    file.write("            }\n")
    file.write("        }\n")
    file.write("        if (td4) {\n")
    file.write("            var txtValue4 = td4.textContent || td4.innerText;\n")
    file.write("            if (txtValue4.toUpperCase().indexOf(filter) > -1) {\n")

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
