import configparser
import praw
import queue


class RedditConnector:
    def __init__(self, thread, COMMENT_COUNT):
        self.thread = thread
        self.COMMENT_COUNT = COMMENT_COUNT

        config = configparser.ConfigParser()
        config.read_file(open("reddit_api_settings.cfg"))

        client_id = config.get("reddit-api", "client_id")
        secret_key = config.get("reddit-api", "secret_key")

        self.reddit = praw.Reddit(
            client_id=client_id,
            client_secret=secret_key,
            user_agent="python:v0.1 (by /u/happykobolt4)"
        )

    def get_thread_queue(self):
        thread_text = queue.Queue()

        thread_obj = self.reddit.submission(url=self.thread)
        thread_obj.comment_sort = "top"

        thread_obj.comments.replace_more(limit=0)

        thread_text.put(thread_obj.title)

        for count, comment in enumerate(thread_obj.comments):
            if count < self.COMMENT_COUNT:
                thread_text.put(comment.body)

        return queue
