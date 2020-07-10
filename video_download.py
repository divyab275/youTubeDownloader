import requests
import urllib.request
import sys
from network_requests import getVideoURL



def downloadVideo(filename,audio_link):
    url_base = getVideoURL(audio_link)

    f = open(filename,'ab')
    
    
    start = 0
    end = 500000
    rn_count  = 2

    while True:
        url = url_base + "range=" + str(start) + "-" + str(end) + "&rn=" + str(rn_count) + "&rbuf=3820"
        try:
            res = requests.get(url)
            print(len(res.content))
            if(len(res.content) == 0):
                break
            f.write(res.content)
        except Exception as exc:
            print("Done...")
            break
        start = end + 1
        end = start + 500000


    f.close()
    return filename

if __name__ == "__main__":
    filename = "video_only/"+sys.argv[1]
    audio_link = sys.argv[2]
    downloadVideo(filename,audio_link)