import pygame, math

class Battery:
    def __init__(self, screen) -> None:
        self.position = pygame.Vector2(100, 100)
        self.screen = screen
        self.color = "blue"
        self.radius = 20
        
    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.position, self.radius)

class LED:
    def __init__(self, screen) -> None:
        self.position = pygame.Vector2(100, 100)
        self.screen = screen
        self.color = "red"
        self.radius = 10

    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.position, self.radius)

def evenly_space_components(component, components:dict):

    distance_away = 50
    
    counter = 1
    for child_component in components[component]:
        if child_component == component:
            continue
        else:
            num_connections = len(components[component])
            print(num_connections)
            spacing = 360/(num_connections + 1)
            print('spacing: ', spacing)
            theta = 180 + spacing*counter
            print(theta)
            theta = math.radians(theta)
            child_component.position = component.position + pygame.Vector2(distance_away*math.cos(theta), distance_away*math.sin(theta))
            counter += 1

def draw(components, screen):
    for component in components:
        for connection in components[component]:
            pygame.draw.line(screen, "black", component.position, connection.position, 4)
    
    for component in components:
        component.draw()

