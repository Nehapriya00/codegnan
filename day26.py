#Date and Time: python provides the built-in datetime module to work with date and time.
#import datetime
'''
#to access today date
import datetime
today=datetime.date.today()
print(today)


#to access today time
import datetime
today=datetime.date.today()
now=datetime.datetime.now()
print(now)
print(today)


#to access year,month,day,hour
import datetime
now=datetime.datetime.now()
print(f"Year is:{now.year}")
print(f"Month is: {now.month}")
print(f"Day is: {now.day}")
print(f"Hour is: {now.hour}")
print(f"Minute is: {now.minute}")
print(f"Seconds is: {now.second}")


#Formatting date and time:
#strftime(): is the method used to formate date and time
#%d--day, %m--month, %Y--year,%H--hour, %M--minute ,%S--second
import datetime
now=datetime.datetime.now()
print(now.strftime("%d-%m-%Y"))
print(now.strftime("%H-%M-%S"))

##
import datetime
date_1=datetime.date(2025,6,1)
date_2=datetime.date(2026,6,1)
diff=date_2-date_1
print(diff)


#timedelta
import datetime
today=datetime.date.today()
future=today+datetime.timedelta(days=7)
print(future)


#ctime():returns readable datetime string
import datetime
day=datetime.date.today()
print(day.ctime())

#to access particular month calender
import calendar
import datetime
today=datetime.date.today()
year=today.year
month=today.month
print(calendar.month(year,month))


#to access total year
import calendar
year=2026
print(calendar.calendar(year))
'''


#program to send email msg in particular time
import smtplib
from email.message import EmailMessage
import time
from datetime import datetime
sender_mail="nehapriya552@gmail.com"
password="xrqmngmizvikrqjd"
receiver_mail="rajanasravyasri@gmail.com"
target_time="10:15"
msg=EmailMessage()
msg["Subject"]="Welcome Mail"
msg["From"]=sender_mail
msg["To"]="rajanasravyasri@gmail.com"
msg.set_content('HIII My self Neha.')
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender_mail,password)
server.send_message(msg)
server.quit()


