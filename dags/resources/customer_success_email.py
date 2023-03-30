import smtplib, ssl
from email.message import EmailMessage

from dagster import (
    resource,
    StringSource
)

@resource(
        config_schema={
            "username": StringSource,
            "password": StringSource,
            "subject": str,
            "message": str
        }
)
def email_sender(init_context):

    HOST = "smtp-mail.outlook.com"
    PORT = 587
    USERNAME = init_context.resource_config["username"]
    PASSWORD = init_context.resource_config["password"]

    msg = EmailMessage()
    msg["Subject"] = init_context.resource_config["subject"]
    msg["From"] = USERNAME
    msg["To"] = "blahblah@blahblah.com"
    msg.set_content(init_context.resource_config["message"])

    server_context = ssl.create_default_context()

    with smtplib.SMTP(HOST, PORT) as server:
        server.ehlo()
        server.starttls(context=server_context)
        server.ehlo()
        server.login(USERNAME, PASSWORD)
        server.send_message(msg)
