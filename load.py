import math
import re

from pydub import AudioSegment

import glob
import os

from youtube_transcript_api import YouTubeTranscriptApi

import youtube_dl

file_number = 1

youtube_video_link = input('Link of the video you want to use: ')

if youtube_video_link.count('?v=') > 0:
    youtube_id = youtube_video_link.split('?v=')[1] # don't change this
else:
    youtube_id = youtube_video_link.split('.be/')[1] # don't change this

# create dir if doesn't exist
os.makedirs(os.path.dirname('input/'), exist_ok=True)
os.makedirs(os.path.dirname('output/'), exist_ok=True)
os.makedirs(os.path.dirname('output/wavs/'), exist_ok=True)

if not len(os.listdir('output/wavs')) == 0:
    list_of_files = glob.glob('output/wavs/*')  # * means all
    latest_file = max(list_of_files, key=os.path.getctime)

    # Extract numbers and cast them to int
    list_of_nums = re.findall('\\d+', latest_file)

    if int(list_of_nums[0]) >= file_number:
        file_number = int(list_of_nums[0]) + 1

ydl_opts = {'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl':'input' + '/%(title)s.%(ext)s',}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([youtube_video_link])

files_in_input = glob.glob('input/*') # * means all if need specific format then *.csv
latest_input_file = max(files_in_input, key=os.path.getctime)

sound_file = AudioSegment.from_file(latest_input_file)
sound_file = sound_file.set_frame_rate(22050)  # don't change this
sound_file = sound_file.set_channels(1)  # don't change this

srt = YouTubeTranscriptApi.get_transcript(youtube_id)

transcription = srt

num_of_sentences = str(transcription).count("'text':")

for sentence in range(num_of_sentences):
    if transcription[sentence]['text'].strip() != '' or transcription[sentence]['text'] is not None:
        print(transcription)
        start_sec = transcription[sentence]['start']

        end_sec = transcription[sentence + 1]['start']

        # Time to miliseconds
        startTime = math.trunc(start_sec * 1000)
        endTime = math.ceil(end_sec * 1000)

        extract = sound_file[startTime:endTime]

        # Saving
        extract.export('output/wavs/' + str(file_number) + '.wav', format="wav")

        transcriptionstring = transcription[sentence]['text'].capitalize().strip().replace('\n', ' ').strip().rstrip(',').rstrip(';').rstrip('.') + '.'

        if os.path.isfile('output/list.txt'):
            if os.stat("output/list.txt").st_size != 0:
                with open('output/list.txt', 'a+', encoding="utf-8") as f:
                    f.write(
                        f'\nwavs/{file_number}.wav|' + transcriptionstring)
                    f.flush()
            else:
                with open('output/list.txt', 'a+', encoding="utf-8") as f:
                    f.write(
                        f'wavs/{file_number}.wav|' + transcriptionstring)
                    f.flush()
        else:
            with open('output/list.txt', 'x', encoding="utf-8") as f:
                f.write(
                    f'wavs/{file_number}.wav|' + transcriptionstring)

        file_number = file_number + 1
