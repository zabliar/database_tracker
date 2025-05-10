import instaloader
from instaloader import Profile

def fetch_account_data_latest_posts(username, num_posts=3):
    L = instaloader.Instaloader()

    try:
        L.load_session_from_file("jack_6581", filename="C:/Users/user/AppData/Local/Instaloader/session-jack_6581")
  # 改成你登入用的帳號名稱
    except FileNotFoundError:
        print("❗ 找不到 session 檔案，請先執行 `instaloader -l your_ig_username` 登入一次")
        return {'followers': 0, 'posts': []}

    if L.context.is_logged_in:
        print("✅ 已使用 session 登入成功！")
        print("登入帳號：", L.test_login())  # 顯示目前登入的帳號
    else:
        print("❌ 尚未登入")

    profile = Profile.from_username(L.context, username)

    followers = profile.followers
    posts = profile.get_posts()

    post_data = []
    for i, post in enumerate(posts):
        if i >= num_posts:
            break
        post_data.append({
            'shortcode': post.shortcode,
            'likes': post.likes,
            'comments': post.comments,
            'timestamp': post.date_utc.strftime("%Y-%m-%d %H:%M:%S")
        })

    return {
        'followers': followers,
        'posts': post_data
    }
