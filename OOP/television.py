class Television:
    def __init__(self): # Constructor
        self.on=False
        self.channel=5
        self.size=25
        self.brand="Panasonic"

    def change_channels(self): # Class method
        a = input("Would you like to go up or down? U/D ")
        if a.upper() == "U":
            self.channel+=1
            print("You are now on channel {}!".format(self.channel))
        elif a.upper() == "D":
            self.channel-=1
            print("You are now on channel {}!".format(self.channel))
        else:
            print("Invalid command!")

tv = Television()
tv.change_channels()