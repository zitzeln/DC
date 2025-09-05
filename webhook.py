import requests
import random
import time
from datetime import datetime
import os

# Get values from GitHub Secrets
url = f"https://discord.com/api/v9/channels/{os.getenv('CHANNEL_ID')}/messages"
token = os.getenv("DISCORD_TOKEN")  # Token

headers = {
    "Authorization": token,  # for user/self-bot
    "Content-Type": "application/json"
}

payload = {
    "content": "What is going on?"
}

# Random wait (0 to 3600 sec = 1 hour)
wait_seconds = random.randint(0, 10)
print(f"Waiting {wait_seconds} seconds before sending...")
time.sleep(wait_seconds)

res = requests.post(url, json=payload, headers=headers)
print(f"[{datetime.now()}] Status: {res.status_code} - {res.text}")
