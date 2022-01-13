import smtplib
from email.message import EmailMessage

def send_alert(subject, message, destination):
    server = smtplib.SMTP('mail.kristijan-projects.xyz', 587)
    server.starttls()
    server.login('alert@kristijan-projects.xyz', '.D,C{=MY7P(a<w;A')

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


