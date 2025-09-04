import requests
import random
import time
from datetime import datetime
import os

# Get webhook URL from GitHub Secrets
url = os.getenv("WEBHOOK_URL")

payload = {"content": "Hello from GitHub Actions!"}

# Random wait (0 to 3600 sec = 1 hour)
wait_seconds = random.randint(0, 3600)
print(f"Waiting {wait_seconds} seconds before sending...")
time.sleep(wait_seconds)

res = requests.post(url, json=payload)
print(f"[{datetime.now()}] Status: {res.status_code}")
