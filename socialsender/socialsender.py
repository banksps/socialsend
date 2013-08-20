#Social networking file analyzer and sender
#written by Phillip Banks Sr.

import smtplib, sys, os
import networks

#command line input socialsender [subject,attach,gmail_user,gmail_pass)
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
sender = 'banksps@gmail.com'
recipient = 'phillip@banksnetworking.com'
subj = sys.argv[1]
body = ""
guser = sys.argv[2]
gpass = sys.argv[3]


def email(eaddr,subj,attch,body):
    "Sends an e-mail to the specified recipient."
    body = "" + body + ""
 
    headers = ["From: " + sender,
           "Subject: " + subj,
           "To: " + recipient,
           "MIME-Version: 1.0",
           "Content-Type: text/html"]
    headers = "\r\n".join(headers)
 
    session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
 
    session.ehlo()
    session.starttls()
    session.ehlo
    session.login(guser,gpass)
    session.sendmail(sender, recipient, headers + "\r\n\r\n" + body)
    session.quit()


    
#Acquire the file


#Destinguish what type of file it is

#Are there any associated files

#Determine what social networks this file applies to

#Convert to necessary formats that apply and report status
    #If there is an error report and move to manual fix folder

#Send to relevant networks from folders and move content for archiving
	#If there is an error report, send log and stop processing
	
#Save log and move to logs folder
