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
def add_edge(v1,v2):
    if v1  not in nodes:
        print(v1,"is not present in the graph")
    elif v2 not in nodes:
        print(v2,"is not present in the graph")
    else:
        index1=nodes.index(v1)
        index2=nodes.index(v2)
        graph[index1][index2]=1
        graph[index2][index1]=1

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
add_edge("a","b")
print("after adding nodes")
print(nodes)
print(graph)
print_graph()