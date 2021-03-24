import pyaudio
import numpy as np
import aubio

import pygame

from threading import Thread

from audio import Audio

from color_utils import FadingColors
from colors_constants import pastel_world_colors, pastel_world_colors_darker
from Scenes.draw import draw_pygame, Screen

import queue
import time

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-input", required=False, type=int, help="Audio Input Device")
parser.add_argument("-f", action="store_true", help="Run in Fullscreen Mode")
args = parser.parse_args()

args.input = 17

p = pyaudio.PyAudio()
devices = [
    p.get_device_info_by_index(i)
    for i in range(p.get_device_count())
]

if not args.input:
    print("No input device specified. Printing list of input devices now: ")
    p = pyaudio.PyAudio()
    for d in devices:
        print("Device number (%i): %s" % (
            devices.index(d),
            [
                d.get('name'),
                d.get("maxInputChannels"),
                d.get("maxOutputChannels")
            ]
        )
              )
    print("Run this program with -input 1, or the number of the input you'd like to use.")
    exit()

pygame.init()

clock = pygame.time.Clock()

viz_audio = Audio()
time.sleep(1)

# setup onset detector
tolerance = 0.8
win_s = viz_audio.buffer_size  # fft
hop_s = win_s // 2  # hop size
onset = aubio.onset("default", win_s, hop_s, viz_audio.samplerate)

stream = viz_audio.stream

q = queue.Queue()


def get_onsets():
    while True:
        try:
            buffer_size = hop_s // 2  # needed to change this to get undistorted audio
            audiobuffer = stream.read(buffer_size, exception_on_overflow=False)
            signal = np.frombuffer(audiobuffer, dtype=np.float32)

            onset_res = onset(signal)

            if onset_res:
                q.put(True)

        except KeyboardInterrupt:
            print("*** Ctrl+C pressed, exiting")
            break


t = Thread(target=get_onsets, args=())
t.daemon = True
t.start()

circle_colors = [
    pygame.Color(color[0], color[1], color[2], 255)
    for color in pastel_world_colors
]

fading_colors = FadingColors(
    number_of_steps=200,
    colors=pastel_world_colors
)

draw_pygame(
 circle_colors=circle_colors,
 fading_colors=fading_colors,
 screen=Screen(),
 q=q
)
stream.stop_stream()
stream.close()
pygame.display.quit()
