# Tacotron2AutoTrim
Auto trim and auto transcription of audio for using in Tacotron 2

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

UPDATE VERSION 1.3:
 - Thanks to the suggestion of user DogBeef on YouTube: https://www.youtube.com/channel/UC1TUqfutiChlw_A0lIkYvVw
 Tacotron2AutoTrim now uses YouTube Transcript Api for the transcription method (+99% accuracy).
 
Steps for using the YouTube Transcript api are:
  1. Convert your audio to video (if you dont have a video editor you can search in google "mp3 to mp4 converter online").
  2. Upload the converted video to YouTube.
  3. Copy the id of the video | Example: if your youtube video url is this one: https://youtu.be/VDiyQub6vpw (just an example) You have to take this part => VDiyQub6vpw
  4. After you copy the id of your video go into the file called "load.py" and change where it says "yourid" in line 32 and put the id of your video inside the apostrophes.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

UPDATE VERSION 1.2:
- Updated transcription method (using deepspeech now it is around 85% accurate). The models are only trained for english lenguage, you can search on the internet other pretrained models for other lenguages.
if you don't want to use deepspeech for any reason (It is recommended to use it) you can change the bool called "use_deepspeech" to False in load.py and it will use the old method (google free speech recognition).

IMPORTANT | HOW TO SETUP DEEPSPEECH
1. Create a folder called deepspeech and cd into that folder, then run this command: 
                                           
       python -m venv .

 The dot at the end is very important (it tells to python to create a virtual enviroment in that folder).

2. Download Sox from here and add it to Path variable (this is for Windows, I don't know exactly what you have to do in other OS): https://sourceforge.net/projects/sox/.
Then just add "C:\Program Files (x86)\sox-{The version that you downloaded here}" to Path variable.

3. Download the deepspeech pretrained models (download the deepspeech-{the version here}-models.pbmm and also the deepspeech-{the version here}-models.scorer) from here: https://github.com/mozilla/DeepSpeech/releases.
Then go to the folder called "deepspeech-models" and add the downloaded models. 
Note: If the models get updated in Mozilla's DeepSpeech repository then you will need to change the name of the version of the models in the load.py file in lines 61, 63, 75 and 76. The current version is 0.9.3

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

UPDATE VERSION 1.1:
- Updated load.py file for skipping long duration files (see bool skip_large_duration_files in load.py, it is set to True by default), and also added funcionality for skipping non transcribed sentences, so you don't have to correct anything manually,         all is automated. 
- You can change how long you would like the limit of duration (in seconds) to be in line 59 in the load.py file (Change the number, default is 12).

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Usage
1. Clone this repository

        git clone https://github.com/gabcodedev/Tacotron2AutoTrim.git

2. Once the repository is cloned into your computer, replace "anything.mp3" located in "input" folder with your input audio files and delete "0.wav" located in "output/wavs" folder. 
These empty files are added to the repository because git doesn't track empty folders.

3. Install requirements.
   
        pip install -r requirements.txt


4. If your audio trimmed files and transcription results are very long, you can change the "min_silence_len" parameter (line 17 in load.py file) according to your needs, so if you want the script to trim sentences when there is a minimum of 1 second you can change it to 1000, it's in 750 right now, so it will trim at 0.75 sec of silence. I found out that it works just fine at this value. You can also change the "silence_thresh" variable to other value to see if it works better in your case.

5. Run
   
        python load.py yourfile.mp3  

(many audio extensions are supported)

For stopping the trimming and transcription at any time go to the active cmd terminal window and press Ctrl+C (This is only for Windows OS). Search in google for the equivalent shortcut in other OS.
