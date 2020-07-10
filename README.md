### Download YouTube Videos and/or Audios

##### Installation steps

###### **Step1**
Run the following command in the terminal to clone the directory


    git clone https://github.com/divyab275/youTubeDownloader.git


###### **Step2**

Run the following command to install all the dependencies.

    pip install -r requirements.txt

You can choose to create a virutal environment and then do this which is the best practice.  

That's it. You are good to go!


##### Executing steps

###### **To Download Audio Only**

When you are runnning for the first time, create an *audio* folder in the root directory.  
This is where all your audio files will be downloaded.  

Run the following command on the terminal

    python audio_download <name_file.mp3> <youtube_link>

*name_file* is the name of the file that you want to save as.  
*youtube_link* is the link of the youtube file.  

The file will be found inside the audio folder.  

###### **To Download Video Only**

When you are runnning for the first time, create an *video_only* folder in the root directory.  
This is where all your video_only files will be downloaded.  

Run the following command on the terminal

    python video_download <name_file.mp4> <youtube_link>

*name_file* is the name of the file that you want to save as.  
*youtube_link* is the link of the youtube file

The file will be found inside the video_only folder.  

###### **To Download Video**

When you are runnning for the first time, create an *video* folder in the root directory.  
This is where all your video files will be downloaded.  

Run the following command on the terminal

    python video_download <name_file.mp4> <youtube_link>

*name_file* is the name of the file that you want to save as.  
*youtube_link* is the link of the youtube file

The file will be found inside the video folder. 