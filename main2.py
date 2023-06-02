import pygame, random



from ElectricalComponents import Battery, LED

width, height = 500, 500

pygame.init()
pygame.display.init()

screen = pygame.display.set_mode((width, height))

# graph
components = {}

# not currently used
wire_tracking = []

# list to contain all components currently on the screen
list_components = []

first_component = Battery(screen, wire_tracking, (200, 200))

def addLED (to_component): 
    components[to_component] = components.get(to_component, []) + [LED(screen, wire_tracking, (random.randint(50, width-50), random.randint(50, height-50)))]

def addBattery (to_component): 
    components[to_component] = components.get(to_component, []) + [Battery(screen, wire_tracking, (random.randint(50, width-50), random.randint(50, height-50)))]

addLED(first_component)

# list_components.append(Battery(screen, wire_tracking, (200, 200)))
# # components.append(Battery(screen, wire_tracking, (300, 300), color = "red"))
# list_components.append(LED(screen, wire_tracking, (400, 200)))


elementDrag = False
nodeDrag = False
showPower = False
breakMode = False

indextodrag = None


while True:
    # fill background
    screen.fill("lightcyan1")

    # for component in list_components:
    #     component.draw()



    for component in components:
        for connection in components[component]:
            pygame.draw.line(screen, "black", component.position, connection.position, 4)
    
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
                addBattery(first_component)
                print("need to change it from adding to first component to adding to the selected component")
            elif event.key == pygame.K_l:
                addLED(first_component)
                print("need to change it from adding to first component to adding to the selected component")
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


            # for component in components:
            #     if component.checkClick(pygame.mouse.get_pos()):
            #         indextodrag = list_components.index(component)
            #         elementDrag = True
            #         break
            #     elif component.checkNodeClick(pygame.mouse.get_pos()):
            #         indextodrag = list_components.index(component)
            #         nodeDrag = True
            #         break
            


        # elif event.type == pygame.MOUSEMOTION:
        #     if nodeDrag:
        #         list_components[indextodrag].dragNode(pygame.mouse.get_pos())
        #         # if a cathode is dragged over the anode of another component, connect them
        #         for component in list_components:
        #             if component.checkNodeClick(pygame.mouse.get_pos()) and (component != list_components[indextodrag]):
        #                 if list_components[indextodrag].wire_out.cathode.checkClick(pygame.mouse.get_pos()):
        #                     list_components[indextodrag].connect("cathode", component)
        #                 elif list_components[indextodrag].wire_in.anode.checkClick(pygame.mouse.get_pos()):
        #                     list_components[indextodrag].connect("anode", component)
        #                 break
                

        #     elif elementDrag:
        #         list_components[indextodrag].dragComponent(pygame.mouse.get_pos())

        elif event.type == pygame.MOUSEBUTTONUP:
            elementDrag = False
            nodeDrag = False

               
    pygame.display.update()
