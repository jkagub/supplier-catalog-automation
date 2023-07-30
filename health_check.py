#!/usr/bin/env python3

import os
import shutil
import psutil
import socket
import emails

# Function to check CPU usage and return True if usage is over 80%
def check_cpu_usage():
    return psutil.cpu_percent(interval=1) > 80

# Function to check disk usage and return True if free space is less than 20%
def check_disk_usage():
    disk_usage = shutil.disk_usage("/")
    return disk_usage.free / disk_usage.total * 100 < 20

# Function to check available memory and return True if less than 500MB
def check_memory_usage():
    available_memory = psutil.virtual_memory().available
    return available_memory < 500 * 1024 * 1024  # 500MB in bytes

# Function to check if "localhost" resolves to "127.0.0.1" and return True if it does
def check_localhost_resolves():
    try:
        socket.gethostbyname("localhost")
        return True
    except socket.error:
        return False

# Function to generate the error message based on the health check results
def generate_error_message():
    error_message = ""
    if check_cpu_usage():
        error_message += "Error - CPU usage is over 80%\n"
    if check_disk_usage():
        error_message += "Error - Available disk space is less than 20%\n"
    if check_memory_usage():
        error_message += "Error - Available memory is less than 500MB\n"
    if not check_localhost_resolves():
        error_message += "Error - localhost cannot be resolved to 127.0.0.1\n"
    return error_message.strip()

# Function to send the error email with the generated error message
def send_error_email(error_message):
    sender = "automation@example.com"
    recipient = "username@example.com"  # Replace with the actual recipient's email
    subject = "Error - Health Check Failed"
    body = "Please check your system and resolve the following issue(s):\n\n" + error_message
    message = emails.generate_email(sender, recipient, subject, body)
    emails.send_email(message)

if __name__ == "__main__":
    # Generate the error message by checking system health
    error_message = generate_error_message()
    
    # If there are any errors, send an email with the error message
    if error_message:
        send_error_email(error_message)
