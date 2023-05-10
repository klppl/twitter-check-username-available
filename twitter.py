import tweepy
import smtplib
from email.message import EmailMessage

# Replace with your own API keys and access tokens from your Twitter Developer account
TWITTER_CONSUMER_KEY = ''
TWITTER_CONSUMER_SECRET = ''
TWITTER_ACCESS_TOKEN = ''
TWITTER_ACCESS_TOKEN_SECRET = ''

# Replace with your email credentials
EMAIL_SENDER = 'username@gmail.com'
EMAIL_PASSWORD = 'app_password@gmail.com'
EMAIL_RECIPIENT = 'notification@email.com'

# Replace with desired username
DESIRED_USERNAME = ''

def initialize_tweepy():
    auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
    auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
    return tweepy.API(auth)

def check_username(api, username):
    try:
        api.get_user(screen_name=username)
        return False
    except tweepy.errors.NotFound:
        return True
    except tweepy.errors.TweepError as e:
        print(f"Error: {e}")
        return False

def send_email_notification(username):
    msg = EmailMessage()
    msg.set_content(f'The Twitter username {username} is available!')

    msg['Subject'] = f'Twitter username {username} is available'
    msg['From'] = EMAIL_SENDER
    msg['To'] = EMAIL_RECIPIENT

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.send_message(msg)

def main():
    api = initialize_tweepy()
    username_to_check = DESIRED_USERNAME

    if check_username(api, username_to_check):
        send_email_notification(username_to_check)
        print(f"Username {username_to_check} is available. Email notification sent.")
    else:
        print(f"Username {username_to_check} is not available.")

if __name__ == '__main__':
    main()
