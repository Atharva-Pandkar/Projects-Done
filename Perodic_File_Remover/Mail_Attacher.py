from sys import *
import time
import smtplib
import urllib.request
import ssl
from email import encoders 
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

def is_connected() :
 try:
      urllib.request.urlopen('http://216.58.192.142',timeout=1)
      return True
 except Exception as err:
      return False
  
def MailSender(path,mail) :
 try :
  print(path)	
  gmail_user= "Atharvapandkat@gmail.com"
  sent_from = gmail_user
  to =mail
  msg = MIMEMultipart()
  msg['From'] = sent_from
  msg['To'] = to
  email_text = "This File was created on %"#%time.ctime()
  subject = """  Log File """
  msg['Subject'] = subject
  msg.attach(MIMEText(email_text,'plain'))
  attach = open(path,"rb")
  p = MIMEBase('application','octet-stream')
  p.set_payload((attach).read())
  encoders.encode_base64(p)
  p.add_header('Content-Disposition',"attach; filename =Log- %s.txt"%time.ctime())	
  msg.attach(p) 
  server= smtplib.SMTP('smtp.gmail.com',587)
  server.ehlo()
  context = ssl.SSLContext(ssl.PROTOCOL_TLS)
  server.starttls(context=context)
  server.login(gmail_user,"pandkar@1")
  text = msg.as_string()
  server.sendmail(sent_from,to,text)
  server.close()
      
 except Exception as e :
  print(e)
   

def Attach (path,mail) :
 try :
  connected = is_connected();
  if connected:
   MailSender(path,mail)
    
 except Exception as e:
  print (e)   

   
   	
