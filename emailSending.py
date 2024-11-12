import smtplib
from email.mime.text import MIMEText

# Gmail SMTP server setup
smtp_server = 'smtp.gmail.com'
smtp_port = 587  # TLS port

# Email content
msg = MIMEText("Body")
sender = 'kshitijbudholiya2006@gmail.com'
recipients = ['kshitijbudholiya@gmail.com', 'shivamsharma22468@gmail.com']
msg['Subject'] = "Subject"
msg['From'] = sender
msg['To'] = ", ".join(recipients)

# Start SMTP session
s = smtplib.SMTP(smtp_server, smtp_port)

# Start TLS for security
s.starttls()

# Login to Gmail
s.login(sender, 'crfc jcgr cpmi bjxq')  # Replace with your Gmail App Password

# Send the email
s.sendmail(sender, recipients, msg.as_string())

# Close the SMTP session
s.quit()
