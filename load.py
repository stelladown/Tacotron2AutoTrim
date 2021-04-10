import re
import sys

import numpy as np
from pydub import AudioSegment
from pydub.silence import split_on_silence

import glob
import os

import wave
import contextlib

import transcribe

import subprocess

from subprocess import Popen, PIPE

skip_large_duration_files = True

use_deepspeech = True

file_number = 1

# assign files
input_file = 'input/' + sys.argv[1]

sound_file = AudioSegment.from_file(input_file)
sound_file = sound_file.set_frame_rate(22050)  # don't change this
sound_file = sound_file.set_channels(1)  # don't change this
audio_chunks = split_on_silence(sound_file, min_silence_len=500,  # 1000 cuts at 1 second of silence. 500 is 0.5 sec
                                silence_thresh=-40)

for i, chunk in enumerate(audio_chunks):

    if len(os.listdir('output/wavs')) == 0:
        print("Wavs directory is empty")
    else:
        list_of_files = glob.glob('output/wavs/*')  # * means all
        latest_file = max(list_of_files, key=os.path.getctime)

        # Extract numbers and cast them to int
        list_of_nums = re.findall('\\d+', latest_file)

        if int(list_of_nums[0]) >= file_number:
            file_number = int(list_of_nums[0]) + 1

    out_file = "output/wavs/{0}.wav".format(file_number)
    print("exporting", out_file)

    chunk.export(out_file, format="wav")

    fname = out_file
    with contextlib.closing(wave.open(fname, 'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
        print('Duration:', duration)

    if skip_large_duration_files:
        if duration < 12:
            if use_deepspeech:
                model_file_path = 'deepspeech-models/deepspeech-0.9.3-models.pbmm'

                scorer_file_path = 'deepspeech-models/deepspeech-0.9.3-models.scorer'

                os.chdir('deepspeech')

                subprocess.call(
                    "Scripts\\activate",
                    shell=True)

                os.chdir('../')

                transcription = subprocess.check_output([
                    "deepspeech",
                    '--model', "deepspeech-models/deepspeech-0.9.3-models.pbmm",
                    "--scorer", "deepspeech-models/deepspeech-0.9.3-models.scorer",
                    "--audio", out_file], shell=True)

                print(transcription)
            else:
                transcription = transcribe.get_large_audio_transcription(out_file)

            if transcription != '':
                if os.path.isfile('output/list.txt'):
                    if os.stat("output/list.txt").st_size != 0:
                        with open('output/list.txt', 'a+') as f:
                            f.write(f'\nwavs/{file_number}.wav|' + transcription.decode('utf-8').capitalize().strip()+'.')
                            f.flush()
                    else:
                        with open('output/list.txt', 'a+') as f:
                            f.write(f'wavs/{file_number}.wav|' + transcription.decode('utf-8').capitalize().strip()+'.')
                            f.flush()
                else:
                    with open('output/list.txt', 'x') as f:
                        f.write(f'wavs/{file_number}.wav|' + transcription.decode('utf-8').capitalize().strip()+'.')

                file_number = file_number + 1
            else:
                os.remove(out_file)
        else:
            os.remove(out_file)

    else:
        transcription = transcribe.get_large_audio_transcription(out_file)

        if transcription != '':
            if os.path.isfile('output/list.txt'):
                if os.stat("output/list.txt").st_size != 0:
                    with open('output/list.txt', 'a+') as f:
                        f.write(f'\nwavs/{file_number}.wav|' + transcription)
                        f.flush()
                else:
                    with open('output/list.txt', 'a+') as f:
                        f.write(f'wavs/{file_number}.wav|' + transcription)
                        f.flush()
            else:
                with open('output/list.txt', 'x') as f:
                    f.write(f'wavs/{file_number}.wav|' + transcription)

            file_number = file_number + 1
        else:
            os.remove(out_file)
