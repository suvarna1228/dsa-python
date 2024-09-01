def add_node(v):
    if v in graph:
        print(v,"is alredy present in the list")
    else:
        graph[v]=[]
def add_edge(v1,v2,cost):
    if v1 not in graph:
       print(v1,"is not present in the graph")
    elif v2 not in graph:
        print(v2,"is not present in the graph")
    else:
        list1=[v2,cost]
        list2=[v1,cost]
        graph[v1].append(list1)
        graph[v2].append(list2)
def delete_node(v):
    if v not in graph:
        print(v,"is not present in the graph")
    else:
        graph.pop(v)
        for i in graph:
            list1=graph[i]
            if v in list1:
                list1.remove(v)

graph={}
add_node("a")
add_node("b")
add_edge("a","b",10)
delete_node("a")
print(graph)