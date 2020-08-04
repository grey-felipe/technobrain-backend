# import os
# from twilio.rest import Client

# from googlevoice import Voice
# from googlevoice.util import input


# def sendsms(number, message):
#     user = os.environ['EMAIL_HOST_USER']
#     password = os.environ['EMAIL_HOST_USER_PASSWORD']

#     voice = Voice()
#     voice.login(user, password)

#     voice.send_sms(number, message)


# def sendsms(sender, recipient):
#     client = Client(os.environ['TWILIO_ACC_SID'],
#                     os.environ['TWILIO_AUTH_TOKEN'])
#     client.api.account.messages.create(
#         to=recipient,
#         from_=sender,
#         body="Hello Test Escalation")
