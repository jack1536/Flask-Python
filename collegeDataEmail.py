import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime
import requests
import json
import pandas as pd
import os
"""
https://github.com/18F/open-data-maker/blob/api-docs/API.md
"""

# Sending Email
def send_email(receiver_email, filename):
    # Credentials
    sender_email = "jdw.coding.projects@gmail.com"
    password = "NX634K&uV"
    
    # Contents
    subject = "Test Email: " + str(datetime.datetime.now())
    body = """\
    Hi,
    Thank you for using this tool! Please see your file attached.

    Please submit feedback at this link:
    """

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email  # Recommended for mass emails

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    # Open PDF file in binary mode
    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email    
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)
        

def filterData(fileName, min_ACT=None):
    df = pd.read_pickle(fileName)
    if min_ACT is None:
        return df
    else:
        return df[(df['latest.admissions.act_scores.midpoint.cumulative']>=min_ACT)]

def college_data_email(reciever_email, csv_filename, min_ACT = None):
    raw_data_location = "dataGeneration/rawData.plk"
    
    df = filterData(raw_data_location, min_ACT)
    df.to_csv(csv_filename)

    send_email(reciever_email, csv_filename)

    if os.path.exists(csv_filename):
        os.remove(csv_filename)


#college_data_email("jackdavidweber@gmail.com", "testFileName.csv", 33)