import pygame

from components import Battery, LED, draw, evenly_space_components

pygame.init()
pygame.display.init()

screen = pygame.display.set_mode((500, 500))

components = {}

first_component = Battery(screen)

def addLED(to_component):
    led = LED(screen)
    components[to_component] = components.get(to_component, []) + [led]
    components[led] = [to_component]


addLED(first_component)




[print(i.position) for i in components]

evenly_space_components(first_component, components)

while True:

    screen.fill("lightcyan1")

    draw(components, screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.display.quit()
                pygame.quit()
            elif event.key == pygame.K_l:
                addLED(first_component)
                evenly_space_components(first_component, components)

    pygame.display.update()
