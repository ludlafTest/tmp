class TV:
    def __init__(self, lenght, width, resolution, speaker_quality):
        self.length = lenght
        self.width = width
        self.resolution = resolution
        self.speaker_quality = speaker_quality

    def remote(self, button_pressed):
        return f'button_pressed: {button_pressed}'

tv1 = TV(90,70,'1080p','very good')
print(tv1.remote(13))