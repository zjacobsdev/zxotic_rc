"""
light module

"""

class Lights:
    def __init__(self,headlights, turn_lights) -> None:
        self.headlights = headlights
        self.turn_signal = turn_lights

    def left_blinker(self):
        return "Turning left"
    def right_blinker(self):
        return "Turning right"

    def brakes_active(self): #boolean
        return "Brake Lights on "

    def headlights_active(self):
        """
        Lowbeam or Highbeam
        """
        return "headlights active"
    
    def taillights_active(self): #boolean
        return "Taillights active"


    def foglights_active(self):  #boolean
        return "fog lighs on"

    def hazard(self):
        return "Harzard Lights on"

    def reverse(self):
        """
        When the car changes gears to Reverse turn on reverse lights
        """
        return "Vehicle reverse lights on"

    def parking(self):
        return "Parking lights active"
    def daytime(self):
        return "daytime lights active"

    def nightMode(self):
        """
        when its night time, brighen lights more
        """