# SMTP package for a given e-mail provider -> yagmail for gmail in this case
import yagmail
import os
import time
from datetime import datetime as dt
"""
NOTE:
To be secure, you should store the email and password in environment variables
For simplicity I just added a fake email and password in variables
"""

# Sender info
manual_email = 'sender_email@gmail.com'
manual_pw = 'sender_password'

# Receiver info
receiver = 'receiver_email@gmail.com'

subject = 'The subject of the email goes here'
contents = """
Content Goes Here
Note the multiline string for the email content
"""

# Adding a while loop and a timer to make it repeat itself in every given amount of seconds
# This loop will complete every 60 seconds, checks the time and if the time is right, it send the message
while True:
    # Adding date-time to check against in the if condition
    now = dt.now()
    # Send the email if the current time is 13:15
    if now.hour == 13 and now.minute == 15:
        # Create a yag object, use the SMTP method to assign the email
        yag = yagmail.SMTP(user=manual_email, password=manual_pw)
        # Send the email, associate
        yag.send(to=receiver, subject=subject, contents=contents)
        # Write a message to the console to let the user know this step was reached and process completed
        print('Email sent')
        # Send the loop back to sleep for 60 seconds or a given amount of time of your choosing
        time.sleep(60)
