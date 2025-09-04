import praw
import os
import csv
from datetime import datetime

# Authenticate with Reddit using GitHub secrets
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    username=os.getenv("REDDIT_USERNAME"),
    password=os.getenv("REDDIT_PASSWORD"),
    user_agent="OnThisDayTamilNaduBot/1.0"
)

subreddit = "TNArasiyal"

# Get today's date
today_key = datetime.utcnow().strftime("%m-%d")  # e.g. "09-04"
today_full = datetime.utcnow().strftime("%B %d")  # e.g. "September 04"

# Read today's event from CSV
events = []
with open("events.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["date"] == today_key:
            events.append(row["event"])

if events:
    title = f"🔔 On This Day in Tamil Nadu - {today_full}"
    body = "## On this day in Tamil Nadu history:\n\n"
    for e in events:
        body += f"- {e}\n"
    body += "\n*(Auto-posted daily using GitHub Actions 🤖)*"

    reddit.subreddit(subreddit).submit(title=title, selftext=body)
    print(f"✅ Posted: {title}")
else:
    print(f"⚠️ No events found for {today_full} in events.csv")

