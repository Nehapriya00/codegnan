#Email Automation Project
'''
SMTP(Simple mail transfer protocol)
this is used to send the emails fro server to another server.
Note:
1.SMTP SSL Port : 465
2.SMTP TLS Port: 587   (import smtplib)
3.Email Message Class: sender mail,resever mail etc..
msg['Subject']='SMTP ON MAIL'
msg['From']='sneder@mail.com'
msg['To']='Receiver@mail.com'

'''

import smtplib
from email.message import EmailMessage
sender = 'nehapriya552@gmail.com'
password ='dmaxbcfytpwgzooa'
msg = EmailMessage()

msg['Subject']='Welcome Mail'
msg['From']= sender
msg['To']='rajanasravyasri@gmail.com'

msg.set_content('HIII My self Neha.')
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender,password)
server.send_message(msg)
server.quit()


#send mail to multiple mails at a time
import smtplib
from email.message import EmailMessage

sender='nehapriya552@gmail.com'
password='lyrlijpbpcerrqai'
receiver=['rajanasravyasri@gmail.com','duddineha31@gmail.com']
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender,password)
for email in receiver:
    msg=EmailMessage()

    msg['Subject']='Welcome Mail'
    msg['From']=sender
    msg['To']=email
    msg.set_content('Hai')

    server.send_message(msg)
server.quit()
