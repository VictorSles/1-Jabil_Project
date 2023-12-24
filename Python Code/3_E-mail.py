#!/usr/bin/env python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
smtp_server = "smtp.gmail.com"
port = 587
email_sender_1 = "israelvictords@gmail.com"
password = "dali vniv jgyr opae"
email_receiver_1 = "israelvic15@gmail.com"
message = MIMEMultipart()
message['From'] = email_sender_1
message['To'] = email_receiver_1
message['Subject'] = "Meu Assunto Teste 2"
body = "Hello, that is my first email send throught Python!! And i WIN!"
message.attach(MIMEText(body, 'plain'))
server = smtplib.SMTP('smtp.gmail.com: 587')    
server.connect('smtp.gmail.com', 587)
server.ehlo
server.starttls()
server.ehlo
server.login(email_sender_1, password)
text = message.as_string()
server.sendmail(email_sender_1, email_receiver_1, text)
server.quit()