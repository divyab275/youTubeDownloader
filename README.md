### Download YouTube Videos and/or Audios

##### Installation steps

###### **Step1**
Run the following command in the terminal to clone the directory


    git clone https://divyab275.github.io/youTubeDownloader.git


###### **Step2**

Run the following command to install all the dependencies.

    pip install -r requirements.txt

You can choose to create a virutal environment and then do this which is the best practice.  

That's it. You are good to go!


##### Executing steps

###### **To Download Audio Only**

Run the following command on the terminal

    python audio_download <name_file.mp3> <youtube_link>

*name_file* is the name of the file that you want to save as.  
*youtube_link* is the link of the youtube file.  

The file will be found inside the audio folder.  

###### **To Download Video Only**

Run the following command on the terminal

    python video_download <name_file.mp4> <youtube_link>

*name_file* is the name of the file that you want to save as.  
*youtube_link* is the link of the youtube file

The file will be found inside the video_only folder.  

###### **To Download Video**

Run the following command on the terminal

    python video_download <name_file.mp4> <youtube_link>

*name_file* is the name of the file that you want to save as.  
*youtube_link* is the link of the youtube file

The file will be found inside the video folder. 