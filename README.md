# Tacotron2AutoTrim
Auto trim and auto transcription of audio for using in Tacotron 2

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

UPDATE VERSION 1.3:
 - Thanks to the suggestion of user DogBeef on YouTube: https://www.youtube.com/channel/UC1TUqfutiChlw_A0lIkYvVw
 Tacotron2AutoTrim now uses YouTube Transcript Api for the transcription method (+99% accuracy).
 
Steps for using the YouTube Transcript api are:
  1. Convert your audio to video (if you dont have a video editor you can search in google "mp3 to mp4 converter online").
  2. Upload the converted video to YouTube (it has to be either a public video or you can also upload it in hidden mode) and enable subtitles in english (or the lenguage of the audio).
  3. Copy the id of the video | Example: if your youtube video url is this one: https://youtu.be/VDiyQub6vpw (just an example) You have to take this part => VDiyQub6vpw
  4. After you copy the id of your video go into the file called "load.py" and change where it says "yourvideoid" in line 32 and put the id of your video inside the apostrophes.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Usage
1. Clone this repository

        git clone https://github.com/gabcodedev/Tacotron2AutoTrim.git

2. Once the repository is cloned into your computer, replace "anything.mp3" located in "input" folder with your input audio files and delete "0.wav" located in "output/wavs" folder. 
These empty files are added to the repository because git doesn't track empty folders.

3. Install requirements.
   
        pip install -r requirements.txt
        
4. Run
   
        python load.py yourfile.mp3  

(many audio extensions are supported)
