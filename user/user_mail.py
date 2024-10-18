# module for email the user for otp verification, update password
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_mail(receiver_email, body, Subject = 'OTP Verification PhraseTest'):

    msg = MIMEMultipart()
    msg['From'] = 'pago.j.bscs@gmail.com'
    msg['To'] = receiver_email
    msg['Subject'] = Subject

    msg.attach(MIMEText(body, 'plain'))


    try:

        sender_mail = 'pago.j.bscs@gmail.com'

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_mail, 'gwli wvaw mted kjux')

        server.sendmail(sender_mail, receiver_email, msg.as_string())

        return True
        

    except Exception as e:

        print(f"Error: {e}")
        return False
    
    finally:

        server.quit()



