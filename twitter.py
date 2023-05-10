import tweepy
import smtplib
from email.message import EmailMessage

# Replace with your own API keys and access tokens from your Twitter Developer account
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

# Replace with your email credentials
email_sender = 'username@gmail.com'
email_password = 'app_password@gmail.com'
email_recipient = 'notificaiton@email.com'

# Replace with desired username
desired_username = ''

# Initialize Tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def check_username(username):
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
    msg['From'] = email_sender
    msg['To'] = email_recipient

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(email_sender, email_password)
        server.send_message(msg)

def main():
    username_to_check = desired_username

    if check_username(username_to_check):
        send_email_notification(username_to_check)
        print(f"Username {username_to_check} is available. Email notification sent.")
    else:
        print(f"Username {username_to_check} is not available.")

if __name__ == '__main__':
    main()
