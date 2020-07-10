from seleniumwire import webdriver  
import re
import sys
import time

def getVideoURL(url):

    driver = webdriver.Firefox()
    driver.get(url)
    vid_count = 0
    aud_count = 0

    for request in driver.requests:
        if request.response:
            # print(request.path)
            try:
                content_type = request.response.headers['Content-Type']
                # print(content_type)
                if(content_type == "video/webm" or content_type == "video/mp4"):
                   vid_url = request.path
                   break
            except Exception as exc:
                # print("PEshakanuuu")
                pass
                
    driver.quit()


    vid_base_url_regex = "(.*)range"
    vid_base_url = re.search(vid_base_url_regex,vid_url).group(1)   
        

    return vid_base_url

def getAudioURL(url):
    driver = webdriver.Firefox()
    driver.get(url)
    vid_count = 0
    aud_count = 0

    for request in driver.requests:
        if request.response:
            # print(request.path)
            try:
                content_type = request.response.headers['Content-Type']
                # print(content_type)
                if(content_type == "audio/webm"):
                   aud_url = request.path
                   break
            except Exception as exc:
                # print("PEshakanuuu")
                pass
                
    driver.quit()

    aud_base_url_regex = "(.*)range"
    aud_base_url = re.search(aud_base_url_regex,aud_url).group(1)

    return aud_base_url

if __name__ == "__main__":
    print(getAudioURL(sys.argv[1]))
    print(getVideoURL(sys.argv[1]))