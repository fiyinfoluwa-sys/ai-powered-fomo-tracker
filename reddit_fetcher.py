import praw

# Initialize the Reddit client with your credentials
reddit = praw.Reddit(
        client_id='BQLAk042OsrL6v48RFcLOQ',
        client_secret='VxFIYknL2Tlf5loyakJbbzVUnim30Q',
        user_agent='fomo-tracker by /u/External-Sherbert-76'
    )


def get_reddit_trends(subreddit_name="popular", limit=5):
    subreddit = reddit.subreddit(subreddit_name)
    hot_posts = subreddit.hot(limit=limit)

    trends = []
    for post in hot_posts:
        if not post.stickied:
            trends.append({
                "title": post.title,
                "score": post.score,
                "url": post.url
            })
    return trends
