# Packet-Sniff - 2 Versions Tool simply analyzes network traffic 

#1. Packets.py collects and oraganizes it into a table located in "output.html" on your desktop. -Laggy when filtering

#2. SqlPacket.py writes to SQL document that you can then use a Node.JS web interface to view and filter. Currently local hosted, Will be server hosted to optimize fitler feed back. Or simply use a free lite SQL reader - does not lag

#Languages
Python(main)
HTML
JavaScript
SQL
Node.JS


#Library:
Scapy
Pycap
sqllite
sqlite3
ejs
enterprise
verbose
winpcap https://www.winpcap.org/install/


#Todo:
-Constant write (threading?)
-Implement capture choices before capture
-Limit duplicate captures - to optimize?
-More OS options than windows
-Show total captures

#Completed
Color Key & Color Cordination
Output to HTML file
Improve filter
Allow custom search/capture of specific traffic
