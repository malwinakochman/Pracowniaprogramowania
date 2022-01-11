class TV():
    
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.volume_level = 0
    
    def turn_on(self):
        self.is_on = True
    
    def turn_off(self):
        self.is_on = False
    
    def set_channel(self,new_channel_no):
        self.channel_no = new_channel_no
        
    def show_status(self):
        if self.is_on == True:
            print(f"TV is on, channel {self.channel_no}, volume {self.volume_level}")
        else:
            print("TV is off")

    def increase_volume(self):
        self.volume_level += 1
    
    def decrease_volume(self):
        self.volume_level -= 1
        
        
        
tv = TV()
tv.show_status()
tv.turn_on()
tv.show_status()
tv.set_channel(5)
tv.increase_volume()
tv.increase_volume()
tv.show_status()
tv.turn_off()
tv.show_status()