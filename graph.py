def add_node(f):
    global node_count
    if f in nodes:
        print(f,"is already present in the graph")
    else:
        node_count=node_count+1
        nodes.append(f)
        for n in graph:
            n.append(0)
        temp=[]
        for i in range(node_count):
            temp.append(0)
        graph.append(temp)
def print_graph():
    for i in range (node_count):
        for j in range(node_count):
            print(graph[i][j],end=" ")
        print()
nodes=[]
graph=[]
node_count=0
print("before adding nodes")
print(nodes)
print(graph)
add_node("a")
add_node("b")
add_node("c")
add_node("d")
add_node("e")
print("after adding nodes")
print(nodes)
print(graph)
print_graph()