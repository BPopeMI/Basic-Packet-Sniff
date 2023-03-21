# Packet-Sniff - 2 Versions Tool simply analyzes network traffic 

#1. Packets.py collects and oraganizes it into a table located in "output.html" on your desktop. -Laggy when filtering

#2. SqlPacket.py writes to SQL database. Use any SQLite viewer to access database content. 
#2.A Using nodeJS script you can turn the SQL database back into an html document format to view the information - Kinda worthless but a friend challenged me to convert it back as practice.

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
-Constant write (threading?) - Works in DB
-Implement capture choices before capture
-Limit duplicate captures - to optimize?
-More OS options than windows
-Show total captures

#Completed
Color Key & Color Cordination
Output to HTML file
SQL Format
Improve filter
Allow custom search/capture of specific traffic
