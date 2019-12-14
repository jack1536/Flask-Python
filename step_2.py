import datetime
import requests
import json
import pandas as pd
import os

import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


json_from_frontend = {
    "is_in" : {
        "school.state": ["TX", "CA","NY","FL"],
        "school.carnegie_basic" : ["Doctoral Universities: Very High Research Activity", "Baccalaureate Colleges: Arts & Sciences Focus"]
        },
    "is_btwn": {
        "latest.admissions.act_scores.midpoint.cumulative" : {
            "min" : 30,
            "max" : 35,
            "inclusive": True,
            },
        "latest.student.demographics.women" : {
            "min":1,
            "max":1,
            "inclusive": True,
         }
     }
}


def is_in_filter(d, df):
    dft = df
    for key in d:
        dft = dft[dft[key].isin(d[key])]
        
    return dft


def is_btwn_filter(d, df):
    dft = df
    for key in d:
        dft = dft[dft[key].between(d[key]['min'], d[key]['max'], inclusive = d[key]['inclusive'])]
        
    return dft


def filter_main(d, df):
    dft = df
    dft = is_btwn_filter(d['is_btwn'], dft)
    dft = is_in_filter(d["is_in"], dft)
    return dft


def send_email(receiver_email, filename):
    # Credentials
    sender_email = "jdw.coding.projects@gmail.com"
    password = "PASSWORD_HERE"
    
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
        

def df_to_email(reciever_email, df):
    filename = "temporary_file.csv"
    
    # Convert from df to csv
    df.to_csv(filename)
    
    # Email the file
    send_email(reciever_email, filename)
    
    # Delete the File
    if os.path.exists(filename):
        os.remove(filename)


def step_2_main(plk_filename, json_from_frontend, recipient_email):
    
    # Read
    df = pd.read_pickle(plk_filename)

    # Filter
    """
    We now filter using the json_from_frontend dictionary which is sent to the backend from the user inputs on the frontend. 
    Note that eventually we will need to convert json into python dictionary using 
    process outlined here: https://www.w3schools.com/python/python_json.asp
    """
    df = filter_main(json_from_frontend, df)
    
    # Send Email
    df_to_email(recipient_email, df)

    
#step_2_main("../step_1_folder/simple_raw_data.plk", json_from_frontend, "jackdavidweber@gmail.com")