import settings
import smtplib
from email.message import EmailMessage


csmtp = settings.smtp
cport = settings.port
caccount = settings.account
cpassword = settings.password
sendAlert = settings.sendAlerts

def send_alert(subject, message, destination):
    server = smtplib.SMTP(csmtp, cport, timeout=120)
    server.starttls()
    server.login(caccount, cpassword)
    if sendAlert:
        try:
            msg = EmailMessage()
            message = f'{message}\n'
            msg.set_content(message)
            msg['Subject'] = subject
            msg['From'] = 'alert@kristijan.me'
            msg['To'] = destination
            server.send_message(msg)
            print("Alert sent via e-mail!")
        except:
            print("Something went wrong. Alert is not sent!")
    else:
        print('Sending e-mail alerts is currently disabled in config.yaml file, please set "send-alerts" to "true" if you want to send e-mails!')


def email_test():
    recipient = settings.testEmail
    subject_alert = "Website Alert Test Email"
    message_alert = "This is an automated email test from your Website Alert application. Email is successfully delivered. Congrats!"
    send_alert(subject_alert, message_alert, recipient)

""" email_test() """ #Uncomment to send a test email to yourself or somebody (set test-eamil address in config.yaml file)