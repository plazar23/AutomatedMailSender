import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

me = "miroljubalert@gmail.com"
you = "plazar23@gmail.com"
msg = MIMEMultipart('alternative')
msg['Subject'] = "555-333 TEST"
msg['From'] = me
msg['To'] = you

pocetakhtmla = '<html><head></head><body><p>'
sredinahtmla = 'Hi!<br>How are you?<br>Here is the <a href="http://www.python.org">link</a> you wanted.'
krajhtmla = '</p></body></html>'

html = pocetakhtmla + sredinahtmla + krajhtmla
part = MIMEText(html, 'html')
msg.attach(part)

mail = smtplib.SMTP('smtp.gmail.com', 587)
mail.ehlo()
mail.starttls()

mail.login('miroljubalert@gmail.com', 'idespodmac')
mail.sendmail(me, you, msg.as_string())
mail.quit()
