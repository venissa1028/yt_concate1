
from pytube import YouTube
from yt_concate1.pipeline.steps.step import Step
from yt_concate1.pipeline.steps.step import StepException


class DownloadCaption(Step):
    def process(self, data, inputs, utils):
        for url in data:
            source = YouTube(url)
            en_caption = source.captions.get_by_language_code('a.en')
            en_caption_convert_to_srt = (en_caption.generate_srt_captions())
            print(en_caption_convert_to_srt)
            # save the caption to a file named Output.txt
            text_file = open(utils.get_caption_path(url), "w")
            text_file.write(en_caption_convert_to_srt)
            text_file.close()
            break

# from pytube import YouTube
# IT IS WORK
#
'''
link = 'https://www.youtube.com/watch?v=wjTn_EkgQRg&index=1&list=PLgJ7b1NurjD2oN5ZXbKbPjuI04d_S0V1K'
src = YouTube(link)
# Getting only English captions by specifying 'en' as parameter
en_caption = src.captions.get_by_language_code('en')
print(en_caption.xml_captions)

# Instead of Captions in XML format we are converting it to string format.
en_caption_convert_to_srt = (en_caption.generate_srt_captions())
print(en_caption_convert_to_srt)
----------------------------------------------------

#(TEACHER CODE)
from pytube import YouTube
from yt_concate1.pipeline.steps.step import Step
from yt_concate1.pipeline.steps.step import StepException


class DownloadCaption(Step):
    def process(self, data, inputs, utils):
        # download the package by:  pip install pytube
        for url in data:
            source = YouTube(url)

            en_caption = source.captions.get_by_language_code('en')
            en_caption_convert_to_srt = (en_caption.generate_srt_captions())
            print(en_caption_convert_to_srt)
            # save the caption to a file named Output.txt
            text_file = open(utils.get_caption_path(url), "w")
            text_file.write(en_caption_convert_to_srt)
            text_file.close()
            break
'''
