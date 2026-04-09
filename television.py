class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    
    def __init__(self):
        """Sets the default instance variables"""
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL
        
    def power(self):
        """Turns the tv on or off using the status variable."""
        if self.__status:
            self.__status = False
        else:
            self.__status = True
    
    def mute(self):
        """Mutes or unmutes the tv when it is on."""
        if self.__status:
            if self.__muted:
                self.__muted = False
            else:
                self.__muted = True
    
    def channel_up(self):
        """Increases the channel by 1 when the tv is on. Goes back to minimum if at maximum."""
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL
    
    def channel_down(self):
        """Decreases the channel by 1 when the tv is on. Goes back to maximum if at minimum."""
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL
    
    def volume_up(self):
        """Increases the volume by 1 when the tv is on. Unmutes if muted. Stays at maximum if already maximum."""
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1
                
    def volume_down(self):
        """Decreases the volume by 1 when the tv is on. Unmutes if muted. Stays at minimum if already minimum."""
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
    
    def __str__(self):
        """Returns current Television state, including: power, channel, and volume."""
        if self.__muted:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
        