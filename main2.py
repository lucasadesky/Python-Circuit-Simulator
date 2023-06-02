import pygame, random



from ElectricalComponents import Battery, LED

width, height = 500, 500

pygame.init()
pygame.display.init()

screen = pygame.display.set_mode((width, height))

# not currently used
wire_tracking = []

# list to contain all components currently on the screen
components = []

components.append(Battery(screen, wire_tracking, (200, 200)))
# components.append(Battery(screen, wire_tracking, (300, 300), color = "red"))
components.append(LED(screen, wire_tracking, (400, 200)))


elementDrag = False
nodeDrag = False
showPower = False
breakMode = False

indextodrag = None


while True:
    # fill background
    screen.fill("lightcyan1")

    for component in components:
        component.draw()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.display.quit()
                pygame.quit()
            elif event.key == pygame.K_b:
                components.append(Battery(screen, wire_tracking, (random.randint(50, width-50), random.randint(50, height-50))))
            elif event.key == pygame.K_l:
                components.append(LED(screen, wire_tracking, (random.randint(50, width-50), random.randint(50, height-50))))
            elif event.key == pygame.K_SPACE:
                breakMode = True
                print("Click a component to break its connection(s)")
            elif event.key == pygame.K_p:
                showPower = True
                print("Click an element to see its power")


        if event.type == pygame.MOUSEMOTION:
            for component in components:
                if component.checkNodeClick(pygame.mouse.get_pos()) or component.checkClick(pygame.mouse.get_pos()):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                    break
                else:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)


        if event.type == pygame.MOUSEBUTTONDOWN:
            if showPower:
                for component in components:
                    if component.checkClick(pygame.mouse.get_pos()):
                        print("power in: ", component.power_in.printPower())
                        print("power out: ", component.getPowerOut().printPower())
                        showPower = False
                        break

            if breakMode:
                for component in components:
                    if component.checkClick(pygame.mouse.get_pos()):
                        component.breakConnection()
                        breakMode = False
                        break

            for component in components:
                if component.checkClick(pygame.mouse.get_pos()):
                    indextodrag = components.index(component)
                    elementDrag = True
                    break
                elif component.checkNodeClick(pygame.mouse.get_pos()):
                    indextodrag = components.index(component)
                    nodeDrag = True
                    break
            


        elif event.type == pygame.MOUSEMOTION:
            if nodeDrag:
                components[indextodrag].dragNode(pygame.mouse.get_pos())
                # if a cathode is dragged over the anode of another component, connect them
                for component in components:
                    if component.checkNodeClick(pygame.mouse.get_pos()) and (component != components[indextodrag]):
                        if components[indextodrag].wire_out.cathode.checkClick(pygame.mouse.get_pos()):
                            components[indextodrag].connect("cathode", component)
                        elif components[indextodrag].wire_in.anode.checkClick(pygame.mouse.get_pos()):
                            components[indextodrag].connect("anode", component)
                        break
                

            elif elementDrag:
                components[indextodrag].dragComponent(pygame.mouse.get_pos())

        elif event.type == pygame.MOUSEBUTTONUP:
            elementDrag = False
            nodeDrag = False

               
    pygame.display.update()
