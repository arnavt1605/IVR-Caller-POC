import os
from twilio.rest import Client

#Used environment variables for defining the variables
account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')

client = Client(account_sid, auth_token)

call = client.calls.create(
    url="---------",   #ngrok generated url
    to="+91--------",  #Receiver's number
    from_="+1--------"              
)

print(f"Started call: {call.sid}")
