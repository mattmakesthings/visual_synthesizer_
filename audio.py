import pyaudio


class Audio:
    def __init__(self):
        self.p = pyaudio.PyAudio()
        self.buffer_size = 1024
        # needed to change this to get undistorted audio
        pyaudio_format = pyaudio.paFloat32
        self.n_channels = 2
        self.samplerate = 44100
        self.stream = self.p.open(
            format=pyaudio_format,
            channels=2,
            rate=self.samplerate,
            input=True,
            # output=True,
            input_device_index=28,
            # output_device_index=21,
            frames_per_buffer=self.buffer_size
        )