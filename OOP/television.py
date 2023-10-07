class Television:
    def __init__(self, min, cur, max): # Constructor
        self.on=False
        self.size=25
        self.brand="Panasonic"
        self.cmin = min
        self.channel = cur
        self.cmax = max

    def change_channels(self): # Class method
        a = input("Would you like to go up or down? U/D ")
        if a.upper() == "U":
            if self.channel + 1 <= self.cmax:
                self.channel +=1
                print("You are now on channel {}!".format(self.channel))
            else:
                raise ValueError("Reached maximum channel!") # Treating exceptions
        elif a.upper() == "D":
            if self.channel - 1 >= self.cmin:
                self.channel-=1
                print("You are now on channel {}!".format(self.channel))
            else:
                raise ValueError("Reached minimum channel!")
        else:
            print("Invalid command!")

tv = Television(0, 5, 100)

while True:
    try:
        tv.change_channels()
    except ValueError as e:
        print(e)
        break