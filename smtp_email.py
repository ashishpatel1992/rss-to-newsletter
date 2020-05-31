import smtplib
import json

config_file_name = "config.json"
with open(config_file_name) as config_file:
    config_data = json.load(config_file)

print(config_data['host'])

# print(config_data[str])

sender = 'test@ashishpatel.dev'
receiver = 'ashishpatel.1992@gmail.com'

message = """TestAsh <test@ashishpatel.dev>
To: Ashish <ashishpatel.1992@gmail.com>
MIME-Version: 1.0
Content-type: text/html
Subject: SMTP HTML e-mail test

This is an e-mail message to be sent in HTML format

<b>This is HTML message.</b>
<h1>This is headline.</h1>
"""

try:
   smtpObj = smtplib.SMTP(config_data['host'])
   smtpObj.login(config_data['username'], config_data['password'])
   smtpObj.sendmail(sender, receiver, message)         
   print ("Successfully sent email")
except Exception as e:
   print ("Error: unable to send email"+e)