# Tacotron2AutoTrim
Auto trim and auto transcription of audio for using in the Tacotron 2 Google Colab project

Usage
1. Clone this repository

        git clone https://github.com/gabcodedev/Tacotron2AutoTrim.git

2. Replace "anything.mp3" located in "input" folder with your input audio files and delete "0.wav" located in "output/wavs" folder. 
These empty files are added to the repository because git doesn't track empty folders.

3. Run
   
        python load.py yourfile.mp3  

(many audio extensions are supported)
