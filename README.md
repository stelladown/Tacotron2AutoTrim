# Tacotron2AutoTrim
Auto trim and auto transcription of audio for using in the Tacotron 2 Google Colab project

Usage
1. Clone this repository

        git clone https://github.com/gabcodedev/Tacotron2AutoTrim.git

2. Once the repository is cloned into your computer, replace "anything.mp3" located in "input" folder with your input audio files and delete "0.wav" located in "output/wavs" folder. 
These empty files are added to the repository because git doesn't track empty folders.

3. You can change the "min_silence_len" parameter (line 20 in load.py file) according to your needs, so if you want the script to trim sentences when there is a minimum of 1 second you can change it to 1000, it's in 750 right now, so it will trim at 0.75 sec of silence. I found out that it works just fine at this value.

4. Run
   
        python load.py yourfile.mp3  

(many audio extensions are supported)
