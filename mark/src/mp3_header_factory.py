from mp3_header import MP3Header


class MP3HeaderFactory:

    @classmethod
    def create(cls, bytes):
        versions = {
            0: "2.5",
            2: "2",
            3: "1",
        }
        layers = {
            0: "III",
            1: "II",
            2: "I",
        }
        bitrate = {
            0: "free",
            1: "32",
            2: "40",
            3: "48",
            4: "56",
            5: "64",
            6: "80",
            7: "96",
            8: "112",
            9: "128",
            10: "160",
            11: "192",
            12: "224",
            13: "256",
            14: "320",
            15: "bad",
        }
        sampling_rates = {
            0: "44100",
            1: "48000",
            2: "32000",
        }
        channel_modes = {
            0: "Stereo",
            1: "Joint Stereo",
            2: "Dual Channel",
            3: "Single Channel",
        }
        mode_extensions = {
            0: "bands 4 to 31",
            1: "bands 8 to 31",
            2: "bands 12 to 31",
            3: "bands 16 to 31",
        }
        emphases = {
            0: "none",
            1: "50/15 ms",
            2: "reserved",
            3: "CCIT J.17",
        }

        version = versions[(bytes[1] & 0x18) >> 3]
        layer = layers[(bytes[1] & 0x06) >> 1]
        protection = (bytes[1] & 0x01)
        bitrate = bitrate[(bytes[2] & 0xF0) >> 4]
        sampling_rate = sampling_rates[(bytes[2] & 0x0C) >> 2]
        padding = (bytes[2] & 0x02) >> 1
        private = (bytes[2] & 0x01)
        channel_mode = channel_modes[(bytes[3] & 0xC0) >> 6]
        mode_extension = mode_extensions[(bytes[3] & 0x30) >> 4]
        copy_right = (bytes[3] & 0x08) >> 3
        original = (bytes[3] & 0x04) >> 2
        emphasis = emphases[(bytes[3] & 0x03)]

        return MP3Header(version, layer, protection, bitrate, sampling_rate, padding, private, channel_mode,
                         mode_extension,
                         copy_right, original, emphasis)
