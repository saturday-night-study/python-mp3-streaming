from pydub import AudioSegment
import numpy as np
from scipy.signal import resample
import lameenc

from .const import KB

from . import model

class MP3Streamer:
    def __init__(self, mp3:model.MP3):
        self.__mp3 = mp3
        self.__audio = AudioSegment.from_mp3(mp3.file_path)
        self.__pcm_data = np.array(self.__audio.get_array_of_samples())
        self.__sample_rate = self.__audio.frame_rate
        self.__channels = self.__audio.channels

    def set_speed(self, output_file:str, speed_factor: float = 1.0):
        num_samples = int(len(self.__pcm_data) / speed_factor)
        adjusted_pcm_data = resample(self.__pcm_data, num_samples)

        encoder = lameenc.Encoder()
        encoder.set_bit_rate(128)
        encoder.set_in_sample_rate(self.__sample_rate)
        encoder.set_channels(self.__channels)
        encoder.set_quality(2)

        mp3_data = encoder.encode(adjusted_pcm_data.tobytes())
        mp3_data += encoder.flush()

        return mp3_data

    def streaming(self):
        with open(self.__mp3.file_path, "rb") as file:
            while chunk := file.read(50 * KB):
                yield chunk