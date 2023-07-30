#!/usr/bin/env python3

from email.message import EmailMessage
import smtplib

# Function to generate an email message
def generate_email(sender, recipient, subject, body, attachment_path=None):
    # Create an EmailMessage object
    message = EmailMessage()
    
    # Set the sender, recipient, and subject fields of the email
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject
    
    # Set the content (body) of the email
    message.set_content(body)
    
    # If an attachment path is provided, add the attachment to the email
    if attachment_path:
        with open(attachment_path, "rb") as file:
            # Read the file content and add it as an attachment
            # The attachment type is set to "application/octet-stream" (generic binary data)
            message.add_attachment(file.read(), maintype="application", subtype="octet-stream", filename=attachment_path)
    
    # Return the generated email message
    return message

# Function to send the email
def send_email(message):
    # Create an SMTP (Simple Mail Transfer Protocol) object with the mail server address ("localhost" in this case)
    mail_server = smtplib.SMTP("localhost")
    
    # Send the email message using the SMTP object
    mail_server.send_message(message)
    
    # Close the connection to the mail server
    mail_server.quit()
