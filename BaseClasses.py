import pygame

def distanceToPoint(point1, point2):
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)**(1/2)

class ElectricalElement:
    def __init__(self, screen:pygame.surface) -> None:
        self.screen = screen
        self.power = Power()
        self.name = None

class Power:
    def __init__(self, current:float = 0.0, voltage:float = 0.0) -> None:
        self.current = current
        self.voltage = voltage

    def printPower(self):
        return "current: ", self.current, " voltage: ", self.voltage
    

    def addPower(self, power):
        return Power(self.current + power.current, self.voltage + power.voltage)


class Node(ElectricalElement):
    def __init__(self, screen, string:type = None, position:tuple = (100, 100)) -> None:
        super().__init__(screen)
        self.type = type # anode or cathode - determines the sign of the voltage
        self.position = position
        self.name = "Node"
        self.radius = 5

    def printType(self):
        print(self.type )

    def checkClick(self, mousePos) -> bool:
        return distanceToPoint(self.position, mousePos) < self.radius+2
    
    def checkClickReturnSelf(self, mousePos):
        if distanceToPoint(self.position, mousePos) < self.radius+2:
            return self
        else:
            return None
    
    def dragNode(self, mousePos):
        self.position = mousePos

class Wire(ElectricalElement):
    def __init__(self, screen, position, in_or_out, wire_tracking) -> None:
        super().__init__(screen)

        if  in_or_out == "in":
            self.cathode = Node(self.screen, "cathode", position)
            self.anode = Node(self.screen, "anode", (position[0] - 0, position[1] + 50))
            self.name = "Wire - in"
        elif in_or_out == "out":
            self.cathode = Node(self.screen, "cathode", (position[0] + 0, position[1] - 50))
            self.anode = Node(self.screen, "anode", position)
            self.name = "Wire - out"
        else:
            raise Exception("Invalid parameter for in_or_out in Wire class")
        
        self.power = Power()
        self.points = []

        # manual properties
        self.width = 5
        self.color = ("darkgray")

    def draw(self, color_override = None):
        self.points = [self.cathode.position, self.anode.position]

        color = self.color

        if color_override != None:
            color = color_override

        # if the anode and cathode are not on the same x or y axis, add a point to the list of points
        if self.cathode.position[0] != self.anode.position[0] or self.cathode.position[1] != self.anode.position[1]:

            # try to maintain original direction of wire
            # if the wire is wire in then the cathode is on top and the anode is on the bottom
            if self.name == "Wire - in":
                self.points.insert(1, (self.cathode.position[0], self.anode.position[1]))
            # if the wire is wire out then the cathode is on the bottom and the anode is on the top
            elif self.name == "Wire - out":
                self.points.insert(1, (self.anode.position[0], self.cathode.position[1]))


        # draw each line segment
        for i in range(len(self.points) - 1):
            start = (self.points[i][0] - self.width//4, self.points[i][1] - self.width//4)
            end = (self.points[i+1][0] - self.width//4, self.points[i+1][1] - self.width//4)
            pygame.draw.line(self.screen, (color), start, end, self.width)

        # add points to list of all points to check for collisions

        # draw the nodes within the wire to create an appearance of rounded corners
        for i in range(1,len(self.points)-1):
            pygame.draw.circle(self.screen, (color), self.points[i], self.width//2)
        
        #draw the start and end nodes
        pygame.draw.circle(self.screen, (color), (self.points[0][0] - self.width//4, self.points[0][1] - self.width//4), self.width)
        pygame.draw.circle(self.screen, (color), (self.points[-1][0] - self.width//4, self.points[-1][1] - self.width//4), self.width)

        

class Component(ElectricalElement):
    def __init__(self, screen, wire_tracking:list, name = "Component", position:tuple = (200, 200)) -> None:
        super().__init__(screen)
        self.position = position
        self.power_in = Power()
        self.wire_in = Wire(self.screen, self.position, "in", wire_tracking)
        self.wire_out = Wire(self.screen, self.position, "out", wire_tracking)
        self.name = name
        self.drag = False
        self.power = Power()


        # self.wire_in.color = "black"
        # self.wire_out.color = "lightcyan1"

    def breakConnection(self):
        self.power_in = Power(0,0)
        self.wire_in.anode.position = (self.position[0] - 0, self.position[1] + 50)
        self.wire_out.cathode.position = (self.position[0] + 0, self.position[1] - 50)

    def connect(self, node_youre_connecting, component):
        """
        Connects a node to a component
        node: anode or cathode (what you are connecting the new component to)
        component: the component you are connecting
        """
        if node_youre_connecting == "anode":
            component.wire_out.cathode.position = self.wire_in.anode.position
            self.power_in = component.getPowerOut()
            
        elif node_youre_connecting == "cathode":
            component.wire_in.anode.position = self.wire_out.cathode.position
            component.power_in = self.getPowerOut()

    def printConnections(self):
        print(self.wire_in)
        print(self.wire_out.cathode.position)
            
    def dragComponent(self, mousePos):
        self.position = mousePos
        self.wire_in.cathode.position = mousePos
        self.wire_out.anode.position = mousePos

    def dragNode(self, mousePos):
        if self.wire_in.anode.checkClick(mousePos):
            self.wire_in.anode.position = mousePos
        elif self.wire_out.cathode.checkClick(mousePos):
            self.wire_out.cathode.position = mousePos

    def checkNodeClick(self, mousePos, return_self = False):
        if return_self:
            return self.wire_in.anode.checkClickReturnSelf(mousePos)       
        else:
            if self.wire_in.anode.checkClick(mousePos):
                return True
            elif self.wire_out.cathode.checkClick(mousePos):
                return True
            else:
                return False
            
    def update(self):
        # check the power of the wire_in
        self.power_in = self.wire_in.power
        # print("this needs to check the power from whatever is connected to it")

            
        



# battery.connect(cathode, LED)