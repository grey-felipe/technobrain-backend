from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django.template.loader import get_template

import smtplib
import os


def send_email(request=None, data=None):
    msg = MIMEMultipart()
    context = dict()

    # create message
    msg['From'] = data['sender']
    msg['To'] = data['recipient']
    msg['Subject'] = data['subject']

    # create body
    body = html_renderer(request, context)

    msg.attach(MIMEText(body, 'html'))

    server = smtplib.SMTP_SSL(host='smtp.gmail.com', port=465)
    server.login(os.environ['EMAIL_HOST_USER'],
                 os.environ['EMAIL_HOST_USER_PASSWORD'])
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()


def html_renderer(request=None, context=None):
    template = get_template('email_template.html')
    return template.render(context, request)