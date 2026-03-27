import time
from screenshot import take_screenshot
from mailer import send_email
from config import INTERVAL, setup_email, EMAIL_SENDER, EMAIL_PASSWORD, EMAIL_RECEIVER


def main():

    print("📸 Auto Screenshot Mailer Started")

    setup_email()

    while True:

        print("Taking screenshot...")

        file_path = take_screenshot()

        print(f"Saved: {file_path}")

        if EMAIL_SENDER:
            print("Sending email...")
            send_email(EMAIL_SENDER, EMAIL_PASSWORD, EMAIL_RECEIVER, file_path)
            print("Email sent!")

        time.sleep(INTERVAL)


if __name__ == "__main__":
    main()
