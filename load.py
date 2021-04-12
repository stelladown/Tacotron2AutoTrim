import re
import sys

from pydub import AudioSegment

import glob
import os

from youtube_transcript_api import YouTubeTranscriptApi

file_number = 1

# assign files
input_file = 'input/' + sys.argv[1]

sound_file = AudioSegment.from_file(input_file)
sound_file = sound_file.set_frame_rate(22050)  # don't change this
sound_file = sound_file.set_channels(1)  # don't change this

if len(os.listdir('output/wavs')) == 0:
    print("Wavs directory is empty")
else:
    list_of_files = glob.glob('output/wavs/*')  # * means all
    latest_file = max(list_of_files, key=os.path.getctime)

    # Extract numbers and cast them to int
    list_of_nums = re.findall('\\d+', latest_file)

    if int(list_of_nums[0]) >= file_number:
        file_number = int(list_of_nums[0]) + 1

srt = YouTubeTranscriptApi.get_transcript("yourvideoid")

transcription = srt

num_of_sentences = str(transcription).count("'text':")

for sentence in range(num_of_sentences):
    if transcription[file_number]['text'] != '' or transcription[file_number]['text'] is not None:
        start_sec = transcription[file_number]['start']

        duration_sec = transcription[file_number + 1]['start']

        difference_time = duration_sec - start_sec

        end_sec = start_sec + difference_time

        # Time to miliseconds
        startTime = start_sec * 1000
        endTime = end_sec * 1000

        extract = sound_file[startTime:endTime]

        # Saving
        extract.export('output/wavs/' + str(file_number) + '.wav', format="wav")

        if os.path.isfile('output/list.txt'):
            if os.stat("output/list.txt").st_size != 0:
                with open('output/list.txt', 'a+') as f:
                    f.write(f'\nwavs/{file_number}.wav|' + transcription[file_number]['text'].capitalize().strip() + '.')
                    f.flush()
            else:
                with open('output/list.txt', 'a+') as f:
                    f.write(f'wavs/{file_number}.wav|' + transcription[file_number]['text'].capitalize().strip() + '.')
                    f.flush()
        else:
            with open('output/list.txt', 'x') as f:
                f.write(f'wavs/{file_number}.wav|' + transcription[file_number]['text'].capitalize().strip() + '.')

        file_number = file_number + 1
