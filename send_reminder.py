from mastodon import Mastodon
from dotenv import load_dotenv
import os
from datetime import datetime


def post_remider():
    # Access the environment variables
    secret_key = os.getenv("SECRET_KEY")
    instance_url = os.getenv("API_BASE_URL")
    account = os.getenv("MASTODON_ACCOUNT")
    message = os.getenv("MESSAGE")
    current_time = datetime.now()
    greeting = "Good morning!! " if current_time.hour < 17 else "Good afternoon!! "
    stretch_reminder = (
        "\n\nPlease have a good stretch and have some water!" if current_time.hour == 18 else ""
    )
    mastodon = Mastodon(
        access_token=secret_key,
        api_base_url=instance_url,
    )
    mastodon.status_post(f"{account}\n\n{greeting}{message}{stretch_reminder}")


def main():
    load_dotenv()
    post_remider()


if __name__ == "__main__":
    main()
