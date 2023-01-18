# Packet-Sniff - 2 Versions Tool simply analyzes network traffic 

#1. Packets.py collects and oraganizes it into a table located in "output.html" on your desktop. -Laggy when filtering

#2. SqlPacket.py writes to SQL database. Use any SQLite viewer to access database content.  Or you can then use a Node.JS script and a web interface to view and filter - Note this converts it back into html table so fitlering is just as laggy as version one. Will also need to install included librarys and node. 

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
-Implement Server Side Filtering for SQL - R730 hosted

#Completed
Color Key & Color Cordination
Output to HTML file
Improve filter
Allow custom search/capture of specific traffic
