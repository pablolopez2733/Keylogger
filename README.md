# Remote Python Keylogger Screenshooter
This is a remote Keylogger/Spyware coded in Python for an Ethical Hacking and Cyber Security undergrad course. Once the script is running, it will log every keystroke and save it to a txt file. Plus, whenever the victim presses ENTER, the script takes a screenshot of the victim's screen and sends the picture and the log file by email. The image and log will de encoded with base 64, so I also  included a script for decoding base 64 text files. whatever you receive by mail should be pasted into the base64-string.txt file.

## DISCLAIMER:
Launching this tool against unauthorised and unwilling users is both immoral and illegal.This tool is for educational purposes only and it is not meant to be used in any harmful way. To reiterate, this tool is meant to be a tool to be studied by white hat hackers and security specialists and is not meant to be deployed against users that do not give you explicit permission. I am not to be held accountable under any circumstances for any illegal, incorrect, or unauthorized use of this code.   

## Files:

* key_log.txt: A txt file in which all the keystrokes are recorded. This is the one you will receive by email. 
* startLogger.sh: A Windows shell script which installs the necessary python libraries and runs the logger.pyw file.
* logger.pyw: The actual script that contains the malware. You may run this script directly if you already have the Pillow and Pynput libraries installed.
* base64-string.txt: Here we paste the base 64 string which we receive by mail. 
* decoder.py: Run this script to decode the base64 encrypted image string. This should return a .png file named 'snap'.

## Important:
Once the script is running, to stop the malware, you must kill the process from the task manager. Otherwise it will continue to log in the background.






