# Sending a customized email to a person.

# Program created by Nadeem Shah.

import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email["From"] = ""
email["To"] = ""
email["Subject"] = "Email from Nadeem"

email.set_content(html.substitute(name=''), 'html') # We can add additional Variables

with smtplib.SMTP("", 587) as smtp:
   smtp.ehlo()
   smtp.starttls()
   smtp.login('', '')
   smtp.send_message(email)
   print("Email sent successfully")


