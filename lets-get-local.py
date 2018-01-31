from twilio.rest import Client
from datetime import datetime

account_sid = "ACCOUNT_SID"
auth_token = "AUTH_TOKEN"

client = Client(account_sid, auth_token)
currenttime = datetime.now().strftime('%H:%M:%S')

message = client.messages.create(
    to="+1234567890",   # Replace phone number
    from_="+14159657284",
    body="Greetings! The current time is: {} NQ3NHO9ABIUJDVV".format(currenttime)
)

print(message.sid)
