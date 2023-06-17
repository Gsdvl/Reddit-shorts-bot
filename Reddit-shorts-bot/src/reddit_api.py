import praw
from reddit_api_config import *

reddit = praw.Reddit(
            username=username,
            password=password,
            client_id=client_id,
            client_secret=client_secret,
            user_agent="praw_scrapper_1.0"
)

file_titulo = open("../reddit_posts/post_titulo_reddit.txt", "a")
file_conteudo = open("../reddit_posts/post_conteudo_reddit.txt", "a")

for submission in reddit.subreddit("desabafos").top(time_filter="week", limit= 1):
    file_titulo.write(submission.title)
    file_conteudo.write(submission.selftext)

file_titulo.close()
file_conteudo.close()