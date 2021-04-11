import firebase_admin
from firebase_admin import credentials, messaging

cred = credentials.Certificate("./serviceAccountKey.json")
firebase_admin.initialize_app(cred)


def send_all():
    registration_token = 'YOUR_REGISTRATION_TOKEN'
    # [START send_all]
    # Create a list containing up to 500 messages.
    messages = [
        messaging.Message(
            notification=messaging.Notification('Price drop', '5% off all electronics'),
            token=registration_token,
        ),
        # ...
        messaging.Message(
            notification=messaging.Notification('Price drop', '2% off all books'),
            topic='readers-club',
        ),
    ]

    response = messaging.send_all(messages)
    # See the BatchResponse reference documentation
    # for the contents of response.
    print('{0} messages were sent successfully'.format(response.success_count))
    # [END send_all]
