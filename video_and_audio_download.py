from moviepy.editor import *
from audio_download import downloadAudio
from video_download import downloadVideo
import os
import sys


def downloadAudioAndVideo(filename,url):

    audio_name = "temp.mp3"
    video_name = "temp.mp4"
    video_file = downloadVideo(video_name,url)
    audio_file = downloadAudio(audio_name,url)
    videoclip = VideoFileClip(video_name)
    audioclip = AudioFileClip(audio_name)
    new_audioclip = CompositeAudioClip([audioclip])
    videoclip.audio = new_audioclip
    videoclip.write_videofile(filename)

    os.remove('temp.mp3')
    os.remove('temp.mp4')

if __name__ == "__main__":
    filename = "video/" + sys.argv[1]
    url = sys.argv[2]
    downloadAudioAndVideo(filename,url)