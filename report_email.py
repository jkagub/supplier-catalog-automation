#!/usr/bin/env python3

import os
import datetime
import reports
import emails

# Directory containing the fruit description text files
input_directory = "supplier-data/descriptions"

# Path to save the processed PDF report
output_file = "/tmp/processed.pdf"

def process_and_send_email():
    # Generate the report title with today's date in the format "Processed Update on Month Day, Year"
    report_title = "Processed Update on {}".format(datetime.date.today().strftime("%B %d, %Y"))
    
    # Initialize an empty string to store the content of the report (paragraph)
    paragraph = ""
    
    # Iterate through each file in the input directory
    for filename in os.listdir(input_directory):
        # Check if the file has a ".txt" extension (assuming it contains the fruit description)
        if filename.endswith(".txt"):
            # Open the file in read mode and read its lines
            with open(os.path.join(input_directory, filename), "r") as file:
                # Read the first line and strip any leading/trailing whitespace to get the fruit name
                name = file.readline().strip()
                
                # Read the second line and strip any leading/trailing whitespace to get the fruit weight
                weight = file.readline().strip()
                
                # Read the third line and strip any leading/trailing whitespace to get the fruit description
                description = file.readline().strip()
                
                # Append the fruit name and weight to the paragraph with appropriate formatting
                paragraph += "name: {}\nweight: {}\n\n".format(name, weight)

    # Generate the PDF report with the processed data (title and paragraph)
    reports.generate_report(output_file, report_title, paragraph)

    # Sender's email address
    sender = "automation@example.com"
    
    # Recipient's email address (Replace with the actual recipient's email)
    recipient = "username@example.com"
    
    # Email subject
    subject = "Upload Completed - Online Fruit Store"
    
    # Email body content
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    
    # Generate the email message with the PDF report as an attachment
    message = emails.generate_email(sender, recipient, subject, body, attachment_path=output_file)
    
    # Send the email using the generated email message
    emails.send_email(message)

if __name__ == "__main__":
    # Call the main function to process and send the email
    process_and_send_email()

