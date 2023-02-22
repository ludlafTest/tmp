class TV:
    def __init__(self, channel):
        self.channel = channel

    def change_channel(self, channel_number):
        if isinstance(channel_number, int):
            self.channel = channel_number
            return self.channel
        else:
            return ("Pls dentrer an integer")

tv1 = TV(4)
new_channel = tv1.change_channel(5)
print(new_channel)