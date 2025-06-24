import os
from twilio.rest import Client

account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')

client = Client(account_sid, auth_token)

call = client.calls.create(
    url="https://6b68-103-174-141-0.ngrok-free.app/voice",   
    to="+919284834031",                
    from_="+16802015441"              
)

print(f"Started call: {call.sid}")
