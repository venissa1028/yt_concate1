# import urllib.request
# import json
# from yt_concate1.settings import API_KEY
# print(API_KEY)

from yt_concate1.pipeline.steps.get_video_list import GetVideoList
from yt_concate1.pipeline.steps.step import StepException

from yt_concate1.pipeline.pipeline import Pipeline
from yt_concate1.pipeline.steps.download_caption import DownloadCaption
from yt_concate1.util import Utils
from yt_concate1.pipeline.steps.preflight import Preflight
from yt_concate1.pipeline.steps.postflight import Postflight

CHANNEL_ID ='UCKSVUHI9rbbkXhvAXK-2uxA'
#teacher

#CHANNEL_ID = 'UCAk3t7WHs2zjsZpopox8Taw' #me


def main():
    inputs = {
        'channel_id': CHANNEL_ID
    }
    steps = [
        Preflight(),
        GetVideoList(),
        DownloadCaption(),
        Postflight(),
    ]

    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils)


if __name__ == '__main__':
    main()

#
'''make pipeline
steps = [
    GetVideoList(),
]

for step in steps:
    try:
        step.process()
    except StepException as e:
        print('Exception happened:', e)
        break

'''

#
'''
def get_all_video_in_channel(channel_id):


    base_video_url = 'https://www.youtube.com/watch?v='
    base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

    first_url = base_search_url + 'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(api_key,
                                                                                                        channel_id)

    video_links = []
    url = first_url
    while True:
        inp = urllib.request.urlopen(url)
        resp = json.load(inp)

        for i in resp['items']:
            if i['id']['kind'] == "youtube#video":
                video_links.append(base_video_url + i['id']['videoId'])

        try:
            next_page_token = resp['nextPageToken']
            url = first_url + '&pageToken={}'.format(next_page_token)
        except KeyError:
            break
    return video_links

'''

# video_list = get_all_video_in_channel(CHANNEL_ID)
# print(len(video_list))
