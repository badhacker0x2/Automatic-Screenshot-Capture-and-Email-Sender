import smtplib
from email.message import EmailMessage

def send_email(sender, password, receiver, file_path):

    msg = EmailMessage()
    msg['Subject'] = 'Automated Screenshot'
    msg['From'] = sender
    msg['To'] = receiver

    msg.set_content("Screenshot attached.")

    with open(file_path, 'rb') as f:
        file_data = f.read()
        file_name = f.name

    msg.add_attachment(file_data, maintype='image', subtype='png', filename=file_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender, password)
        smtp.send_message(msg)
