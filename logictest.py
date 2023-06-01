
class Battery:
    def __init__(self) -> None:
        self.input = None
        self.output = None
        self.type = 'supply'
        self.name = 'battery'
        self.resistance = 0
        self.voltage = 5
        self.current = 1

class LED:
    def __init__(self, name) -> None:
        self.input = None
        self.output = None
        self.type = 'load'
        self.name = 'LED ' + str(name)
        self.resistance = 1000
        self.voltage = 0
        self.current = 0

components = []

components.append(Battery())
components.append(LED('1'))
components.append(LED('2'))
components.append(LED('3'))

def connect(component, newComponent):
    if component.output != None:
        component.output = [component.output, newComponent]
    else:
            component.output = newComponent
    newComponent.input = component

connect(components[0], components[1])
connect(components[1], components[2])
connect(components[1], components[3])
connect(components[3], components[0])
connect(components[2], components[0])

def draw(component, startComponent):
    if component.output == startComponent:
        print(component.name, "->")
        return component.name
    else:
        if type(component.output) == list:
            txt = ""
            for i in range(len(component.output)):
                txt += component.output[i].name + " | "
            print(txt, "-> ")
            draw(component.output[0], startComponent)
        else:
            print(component.name, "-> ")
            draw(component.output, startComponent)



def closedCircuit(components):
    startComponent = components[0]
    contains = f'Loop contains: {startComponent.name}'

    if startComponent.output == None:
        return False
    
    if type(startComponent.output) == list:
        currentComponent = startComponent.output[0]
        multipleOutputs = True
    else:
        currentComponent = startComponent.output

    while currentComponent != startComponent:
        contains += f', {currentComponent.name}'

        loopsremaining = 1
        count = 0

        while loopsremaining > 0:
        
            if type(currentComponent.output) == list:
                loopsremaining = len(currentComponent.output) - count
                currentComponent = currentComponent.output[count]

                
            else:
                currentComponent = currentComponent.output
                loopsremaining = 0

            count += 1

        if currentComponent == None:
            return False
        if currentComponent == startComponent:
            return True, contains
        

# print(closedCircuit(components))

draw(components[0], components[0])