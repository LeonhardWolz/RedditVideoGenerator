import queue

from moviepy.editor import *

test = "Which cheap and mass-produced item is stupendously well engineered?"


class VideoCreator:

    def create(self, thread_text):
        txt_clip = TextClip(test, fontsize=20, color="green").set_duration(10).set_fps(15)

        txt_clip.write_videofile("test.mp4")
