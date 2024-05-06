from twilio.rest import Client
import smtplib

MY_EMAIL = "testmailop001@gmail.com"
MY_PASSWORD = "pass"


TWILIO_SID = "twiliosid"
TWILIO_AUTH_TOKEN = "auth_token"
TWILIO_VIRTUAL_NUMBER = "+number"
TWILIO_VERIFIED_NUMBER = "+number"


class NotificationManager:
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(f"Message Sid: {message.sid}")

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode(
                        "utf-8"
                    ),
                )
