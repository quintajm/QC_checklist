# QC_checklist
Pywebio based local webpage -p 8986 to log visual inspection of TE units
Dec 7, 2021
Setup instructions for local website

With the files on the QC hub just run python main.py
*In this case, the file is on the desktop so we have to add the whole location to the command : /home/pi/Desktop/2000_QC_capturing_QC.com/main.py

After running the script there will be a website that can be accessed while on the local wifi network by going to the QChub’s IP address (10.0.0.21:8986 in this case) on any browser.

Fill in the information and press “SAVE RESULTS”, this will save the information to the QChub in the “data” folder as a .db and backed up as JSON.


