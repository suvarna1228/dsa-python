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
            for j in list1:
             if v ==j[0]:
                list1.remove(j)
                break

graph={}
add_node("a")
add_node("b")
add_node("c")
add_node("d")
add_node("f")

add_edge("a","b",10)
add_edge("b","e",3)
add_edge("a","c",5)
add_edge("a","d",4)
add_edge("b","d",7)
add_edge("c","d",1)
add_edge("e","d",2)


print(graph)
delete_node("c")
print()
print(graph)