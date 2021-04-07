# Tacotron2AutoTrim
Auto trim and auto transcription of audio for using in Tacotron 2


UPDATE VERSION 1.1:
- Switched to sphinx speech recognition.
- Updated load.py file for skipping long duration files (see bool skip_large_duration_files in load.py, it is set to True by default), and also added funcionality for skipping non transcribed sentences, so you don't have to correct anything manually,         all is automated. 
- You can change how long you would like the limit of duration (in seconds) to be in line 55 in the load.py file (Change the number, default is 12).


Usage
1. Clone this repository

        git clone https://github.com/gabcodedev/Tacotron2AutoTrim.git

2. Once the repository is cloned into your computer, replace "anything.mp3" located in "input" folder with your input audio files and delete "0.wav" located in "output/wavs" folder. 
These empty files are added to the repository because git doesn't track empty folders.

3. Install requirements.
   
        pip install -r requirements.txt


4. If your audio trimmed files and transcription results are very long, you can change the "min_silence_len" parameter (line 20 in load.py file) according to your needs, so if you want the script to trim sentences when there is a minimum of 1 second you can change it to 1000, it's in 750 right now, so it will trim at 0.75 sec of silence. I found out that it works just fine at this value. You can also change the "silence_thresh" variable to other value to see if it works better in your case.

5. Run
   
        python load.py yourfile.mp3  

(many audio extensions are supported)

For stopping the trimming and transcription at any time go to the active cmd terminal window and press Ctrl+C (This is only for Windows OS). Search in google for the equivalent shortcut in other OS.
