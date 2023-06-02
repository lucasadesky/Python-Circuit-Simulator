graph = {}

graph['b1'] = ['r1']
graph['r1'] = ['r2', 'r3', 'r4']
graph['r2'] = ['r5']
graph['r3'] = ['b1']
graph['r4'] = ['r5']
graph['r5'] = ['b1']

def next_node(node):
    return graph[node]

# this needs improvement
def findLoop(graph):
    """
    Returns a list of nodes that are in a loop
    """
    loop = []
    for node in graph:
        if graph[node] in loop:
            return loop
        else:
            loop.append(graph[node])
    return loop

print(findLoop(graph))
