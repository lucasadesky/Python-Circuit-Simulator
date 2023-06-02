import pygame

from components import Battery, LED, draw, choose_children_position

pygame.init()
pygame.display.init()

screen = pygame.display.set_mode((500, 500))

components = {}

first_component = Battery(screen)

def addLED():
    led = LED(screen)
    components[first_component] = components.get(first_component, []) + [led]
    components[led] = [first_component]


addLED()


[print(i.position) for i in components]

choose_children_position(first_component, components)

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
                addLED()
                choose_children_position(first_component, components)

    pygame.display.update()
