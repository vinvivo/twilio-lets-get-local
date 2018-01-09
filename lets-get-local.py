from twilio.rest import Client
from datetime import datetime

account_sid = "AC05c492100ba229f40bd463f0c99da9b2"
auth_token = "bf7c0153a0a3ff0dc7fa2ad5e0b532be"

client = Client(account_sid, auth_token)
currenttime = datetime.now().strftime('%H:%M:%S')

message = client.messages.create(
    to="+14153007522",
    from_="+14159657284",
    body="Greetings! The current time is: {} NQ3NHO9ABIUJDVV".format(currenttime)
)

print(message.sid)
