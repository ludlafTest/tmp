class Appliance:
    def __init__(self, input_type):
        self.input_type = input_type

    def switch_on(self):
        return f'switched on using {self.input_type}'


class TV(Appliance):
    def __init__(self, input_type, channel):
        Appliance.__init__(input_type, True)
        self.channel = channel
    def change_number(self, channel_number):
        if isinstance(channel_number, int):
            self.channel = channel_number
        else:
            return "pls enter an integer"


class WashingMachine(Appliance):
    # def __init__(self, input_type, channel):
    #     Appliance.__init__(input_type)
    def wash(self):
        return f'washing your clothes :)'

print('TV')
tv1 = TV(4, 'electricity')
print(tv1.input_type)
print(tv1.switch_on())
print(f"channel number : {tv1.change_number(5)}")

print('\nWashing Machine')
washing_machine1 = WashingMachine('electricity')
print(washing_machine1.input_type)
print(washing_machine1.wash())
print(washing_machine1.switch_on())