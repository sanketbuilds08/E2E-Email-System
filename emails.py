import smtplib
from email.mime.text import MIMEText

def send_email(subject, body):
    sender = "beuniquee2004@gmail.com"
    password = "pgiw cpgx fuus ngkf"  # App password (NOT Gmail password)
    to = "project-team@example.com"
    cc = "team-leads@example.com"
    bcc = "manager@example.com"

    recipients = [to, cc, bcc]
    msg = MIMEText(body, 'plain')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = to
    msg['Cc'] = cc

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(sender, password)
            smtp.sendmail(sender, recipients, msg.as_string())
        return True
    except Exception as e:
        print("Email failed:", e)
        return False
