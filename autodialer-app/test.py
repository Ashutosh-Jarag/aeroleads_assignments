from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()
client = Client(os.getenv("TWILIO_ACCOUNT_SID"), os.getenv("TWILIO_AUTH_TOKEN"))

call = client.calls.create(
    to="+919527900909",  # your verified number
    from_="+18083785769",  # your Twilio number
    twiml="<Response><Say>Hello Ashutosh! This is a test call from your Twilio AutoDialer app.</Say></Response>"
)
print("✅ Call initiated! SID:", call.sid)
