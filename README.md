# Packet-Sniff - 2 Versions
Tool simply analyzes network traffic - collects and oraganizes it into a table located in "output.html" on your desktop.
Currently only works on windows.

One Version writes to a html document - Laggy not recommended
Other Version writes to SQL document that you can then use a Node.JS web interface to view and filter

#Languages
Python(main)
HTML(output and table)
JavaScript(filter ability)
SQL
Node.JS


#Library:
Scapy
Pycap
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
