import praw


def get_hot(amount, score=100):
    r = praw.Reddit('bot1', user_agent='hiphopheads_fresh_sorter')
    submissions = [x.title for x in r.subreddit('hiphopheads').hot(limit=amount) if x.score > score and "[FRESH]" in x.title]
    return submissions
