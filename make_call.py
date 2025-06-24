import os
from twilio.rest import Client

# Use environment variables with correct keys
account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')

client = Client(account_sid, auth_token)

call = client.calls.create(
    url="https://handler.twilio.com/twiml/EHe33336e2fbd8ad6e09a6101125277fcd",
    to="+919284834031",
    from_="+16802015441",
)

print(call.sid)
