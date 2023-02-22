
import os
from yt_concate1.settings import CATION_DIR
from yt_concate1.settings import VIDEO_DIR
from yt_concate1.settings import DOWNLOADS_DIR


class Utils:
    def __init__(self):
        pass

    def create_dir(self):
        os.makedirs(DOWNLOADS_DIR,exist_ok=True)
        os.makedirs(VIDEO_DIR, exist_ok=True)
        os.makedirs(CATION_DIR, exist_ok=True)



    @staticmethod
    def get_video_id_from_url(url):
        return url.split('watch?v=')[-1]

    def get_caption_path(self,url):
        return os.path.join(CATION_DIR,self.get_video_id_from_url(url) + '.txt')
