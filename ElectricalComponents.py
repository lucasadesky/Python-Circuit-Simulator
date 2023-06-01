import pygame

from BaseClasses import Component, Wire, Power

class Battery(Component):
    def __init__(self, screen, wire_tracking_in, position:tuple = (100, 100), color = 'blue') -> None:
        super().__init__(screen, wire_tracking_in, "Battery",position)
        self.color = color
        self.plus_minus_color = "black"
        self.power_in = Power()
        self.power = Power(1, 5)

    def draw(self):
        verticalShift = 5

        self.wire_in.draw("lightseagreen")
        self.wire_out.draw("lightcoral")
        pygame.draw.circle(self.screen, (self.color), self.position, 20)
        # put a plus sign on the battery
        pygame.draw.line(self.screen, self.plus_minus_color, (self.position[0] - 5, self.position[1] - verticalShift), (self.position[0] + 4, self.position[1] - verticalShift), 2)
        pygame.draw.line(self.screen, self.plus_minus_color, (self.position[0] - 1, self.position[1] - 4 - verticalShift), (self.position[0] - 1, self.position[1] + 5 - verticalShift), 2)

        # put a minus sign on the battery
        pygame.draw.line(self.screen, self.plus_minus_color, (self.position[0] - 5, self.position[1] + verticalShift), (self.position[0] + 4, self.position[1] + verticalShift), 2)

        # print("Battery: ", self.getPowerOut().printPower())

    def checkClick(self, mousePos) -> bool:
        if(mousePos[0] > self.position[0] - 20 and mousePos[0] < self.position[0] + 20):
            if(mousePos[1] > self.position[1] - 20 and mousePos[1] < self.position[1] + 20):
                return True
            
    def getPowerOut(self):
        """add the battery's power to the power_in"""
        return Power(self.power.current, self.power_in.voltage + self.power.voltage)

class LED(Component):
    def __init__(self, screen, wire_tracking_in, position:tuple = (100, 100), color = 'red') -> None:
        super().__init__(screen, wire_tracking_in, "LED", position)
        self.color = color

    def draw(self):
        self.wire_in.draw("lightseagreen")
        self.wire_out.draw("lightcoral")
        self.checkIllumination()
        pygame.draw.circle(self.screen, (self.color), self.position, 10)

        # print("LED in: ", self.power_in.printPower())
        # print("LED out: ", self.getPowerOut().printPower())

        
    def checkClick(self, mousePos) -> bool:
        if(mousePos[0] > self.position[0] - 10 and mousePos[0] < self.position[0] + 10):
            if(mousePos[1] > self.position[1] - 10 and mousePos[1] < self.position[1] + 10):
                return True
            
    def getPowerOut(self):
        """reduced the voltage by 1"""
        return Power(self.power_in.current, self.power_in.voltage - 1)
    
    def checkIllumination(self):
        if self.power_in.voltage > 3 and self.power_in.current > 0.5:
            self.color = "greenyellow"
        else:
            self.color = "darkgreen"



            


