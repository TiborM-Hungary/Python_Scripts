# Download the helper library from https://www.twilio.com/docs/python/install
import os
import time
import dt as dt
from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
# NOTE: it is safer to create an environment variable, but you can hard code it in the script if you wish
"""
Environment variables are more secure than plaintext files, 
because they are volatile/disposable, not saved; i.e. if you set only a local environment variable, 
like "set pwd=whatever," and then run the script, 
with something that exits your command shell at the end of the script, 
then the variable no longer exists.
"""

# IF you are not using environment variables, just replaces the os.environ items with your actual account_sid and auth_token
account_sid = os.environ['YOUR_TRILIO_SID']
auth_token = os.environ['YOUR_TRILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

# Try to send an SMS in every 60 seconds, but only if the time is 18:30
while True:
    now = dt.now()
    if now.hour == 18 and now.minute == 30:
        message = client.messages \
            .create(
                body="Testing daily message - 18:30",
                from_='YOUR_TRILIO_PHONE_NUMBER',
                to='YOUR_OWN_PHONE_NUMBER'
            )

        print(message.sid)
    time.sleep(60)
