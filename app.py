from flask import Flask, render_template, jsonify
from database import init_db, fetch_follower_data, fetch_post_data
from scheduler import start_scheduler

app = Flask(__name__)
init_db()
start_scheduler()

@app.route('/')
def index():
    follower_records = fetch_follower_data()
    post_records = fetch_post_data()

    if follower_records:
        timestamps, followers = zip(*follower_records)
    else:
        timestamps, followers = [], []

    return render_template(
        'index.j2',
        timestamps=timestamps,
        followers=followers,
        posts=post_records
    )

@app.route('/api/data')
def api_data():
    follower_records = fetch_follower_data()
    if follower_records:
        latest = follower_records[-1]
        return jsonify({
            'timestamp': latest[0],
            'followers': latest[1]
        })
    else:
        return jsonify({'error': 'No data'})

@app.route('/api/posts')
def api_posts():
    post_records = fetch_post_data()
    posts = []
    for row in post_records:
        posts.append({
            'shortcode': row[0],
            'timestamp': row[1],
            'likes': row[2],
            'comments': row[3]
        })
    return jsonify(posts)

if __name__ == '__main__':
    app.run(debug=True)
