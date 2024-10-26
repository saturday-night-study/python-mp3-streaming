KB = 1024
MB = KB * 1024
GB = MB * 1024

SYNC_WORD_MASK = 0b11111111111
VERSION_MASK = 0b11
LAYER_MASK = 0b11
PROTECTION_MASK = 0b1
BITRATE_MASK = 0b1111
SAMPLING_RATE_MASK = 0b11
PADDING_MASK = 0b1
PRIVATE_MASK = 0b1
CHANNEL_MODE_MASK = 0b11
MODE_EXTENSION_MASK = 0b11
COPYRIGHT_MASK = 0b1
ORIGINAL_MASK = 0b1
EMPHASIS_MASK = 0b11

BITRATE_TABLE = [
    [
        [0],                                                                        # Reserved
        [0, 8, 16, 24, 32, 40, 48, 56, 64, 80, 96, 112, 128, 144, 160],             # MPEG-2.5 Layer 3
        [0, 8, 16, 24, 32, 40, 48, 56, 64, 80, 96, 112, 128, 144, 160],             # MPEG-2.5 Layer 2
        [0, 32, 48, 56, 64, 80, 96, 112, 128, 144, 160, 176, 192, 224, 256],        # MPEG-2.5 Layer 1
    ],
    [
        # Reserved
        [0],    
        [0],    
        [0],    
        [0],    
    ],
    [
        [0],                                                                        # Reserved
        [0, 8, 16, 24, 32, 40, 48, 56, 64, 80, 96, 112, 128, 144, 160],             # MPEG-2 Layer 3
        [0, 8, 16, 24, 32, 40, 48, 56, 64, 80, 96, 112, 128, 144, 160],             # MPEG-2 Layer 2
        [0, 32, 48, 56, 64, 80, 96, 112, 128, 144, 160, 176, 192, 224, 256]         # MPEG-2 Layer 1
    ],
    [
        [0],                                                                        # Reserved
        [0, 32, 40, 48, 56, 64, 80, 96, 112, 128, 160, 192, 224, 256, 320],         # MPEG-1 Layer 3
        [0, 32, 48, 56, 64, 80, 96, 112, 128, 160, 192, 224, 256, 320, 384],        # MPEG-1 Layer 2
        [0, 32, 64, 96, 128, 160, 192, 224, 256, 288, 320, 352, 384, 416, 448]      # MPEG-1 Layer 1
    ]
]

SAMPLE_RATE_TABLE = [
    [11025, 12000, 8000],   # MPEG2.5
    [0, 0, 0],              # Reserved
    [22050, 24000, 16000],  # MPEG2
    [44100, 48000, 32000],  # MPEG1
]
