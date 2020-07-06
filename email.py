import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

def sendEmail(email, message):
    msg = MIMEMultipart()
    msg['Subject'] = 'Graph of data collected for COVID 19 Cases in India'
    msg['From'] = 'add_your_email'
    msg['To'] = email

    text = MIMEText('Pie Chart: National Scale, Bar Chart: Statewise Plot')
    msg.attach(text)

    s = smtplib.SMTP('smtp.gmail.com', 587)
    
    s.starttls()

    s.login("add_your_email", "add_your_password")
    s.sendmail("add_your_email", email, msg.as_string())
    s.quit()

    return ("Please check your mail for the Graphs from Aditya Singh and Thank You for using Panther's email service ;)")
