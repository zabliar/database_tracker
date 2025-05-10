from apscheduler.schedulers.background import BackgroundScheduler
from tracker import fetch_account_data_latest_posts
from database import insert_follower_data, insert_post_data
import config

def scheduled_job():
    try:
        data = fetch_account_data_latest_posts(config.TARGET_USERNAME)
        
        # 儲存粉絲數（單一數字）
        insert_follower_data(data["followers"])
        
        # 儲存每篇貼文的資料
        for post in data["posts"]:
            insert_post_data(
                shortcode=post["shortcode"],
                likes=post["likes"],
                comments=post["comments"],
                timestamp=post["timestamp"]
            )

        print("Data inserted:", data)
    except Exception as e:
        print("Error during scheduled job:", e)

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(scheduled_job, 'interval', seconds=30)  # 可以改回 30 秒
    scheduler.start()
