import smtplib

sender = 'Hector Quemada<hector.quemada@wmich.edu>'
receivers = ['kffhquay@sharklasers.com']

message = """From: 'Hector Quemada<hector.quemada@wmich.edu>'
To: Test person<kffhquay@sharklasers.com>
MIME-Version: 1.0
Content-type: text/html
Subject: SMTP HTML e-mail test

This is an e-mail message to be sent in HTML format<br>

<p><b>This is an HTML message.</b></p>
<h1>This is a headline.</h1>
<p>This is the body of my message</p>
"""

try:
   server = smtplib.SMTP('smtp.office365.com',587)
   server.starttls()
   server.login('hquemada@wmich.edu','TheN3xtD@yAt1')
   server.sendmail(sender, receivers, message)
   print("Successfully sent email")
except SMTPException:
   print("Error: unable to send email")