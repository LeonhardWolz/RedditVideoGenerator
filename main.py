import configparser

from reddit_connector import RedditConnector
from video_creator import VideoCreator



def main():
    config = configparser.ConfigParser()
    config.read_file(open("settings.cfg"))

    thread = config.get("reddit-thread", "thread")
    COMMENT_COUNT = int(config.get("settings", "COMMENT_COUNT"))



    # tts = gTTS(test, lang="en")
    # tts.save("temp/testaudio.mp3")

    #VideoCreator().create(RedditConnector(thread, COMMENT_COUNT).get_thread_queue())
    VideoCreator().create(None)
    # delete temp folder contents


if __name__ == '__main__':
    main()
