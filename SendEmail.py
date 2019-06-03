import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def SendEmail():
    fromaddr = "trymelater3@gmail.com"
    toaddr = "prashantgautamofficial@gmail.com"

    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "INTRUDER ALERT !"
    body = "We Have an Unknown person or an Intruder at the Security check."

    msg.attach(MIMEText(body, 'plain'))
    filename = "intruder.jpg"
    attachment = open(filename, "rb")
    p = MIMEBase('application', 'octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(p)
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(fromaddr, "trymelater")
    text = msg.as_string()
    s.sendmail(fromaddr, toaddr, text)
    s.quit()