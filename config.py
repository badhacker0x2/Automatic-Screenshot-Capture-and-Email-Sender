INTERVAL = 30  # seconds

EMAIL_SENDER = None
EMAIL_PASSWORD = None
EMAIL_RECEIVER = None


def setup_email():
    global EMAIL_SENDER, EMAIL_PASSWORD, EMAIL_RECEIVER

    choice = input("Enable email sending? (y/n): ").lower()

    if choice == "y":
        EMAIL_SENDER = input("Enter sender email: ")
        EMAIL_PASSWORD = input("Enter app password: ")
        EMAIL_RECEIVER = input("Enter receiver email: ")
