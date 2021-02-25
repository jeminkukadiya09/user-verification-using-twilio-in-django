import os
from twilio.rest import Client

account_sid = 'AC*******************************'
auth_token = '12*********************************'
client = Client(account_sid, auth_token)


def send_sms(user_code, phone_number):
	message = client.messages.create(body=f'hi! your user and verification code is {user_code}',
	 from_ ='*************', 
	 to=f'************')



	print(message.sid)