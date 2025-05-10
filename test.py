from tracker import fetch_account_data_latest_posts
import config

data = fetch_account_data_latest_posts(config.TARGET_USERNAME)

print("Followers:", data["followers"])
for i, post in enumerate(data["posts"], start=1):
    print(f"Post {i} ({post['timestamp']}):")
    print("  Shortcode:", post["shortcode"])
    print("  Likes:", post["likes"])
    print("  Comments:", post["comments"])
