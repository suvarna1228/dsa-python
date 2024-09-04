def add_node(v):
    if v in graph:
        print(v,"is alredy present in the list")
    else:
        graph[v]=[]
def add_edge(v1,v2):
    if v1 not in graph:
       print(v1,"is not present in the graph")
    elif v2 not in graph:
        print(v2,"is not present in the graph")
    else:
        #list1=[v2,cost]
        #list2=[v1,cost]
        graph[v1].append(v1)
        graph[v2].append(v2)

def dfs(node,visited,graph):
    if node  not in graph:
        print("node is not present in the graph")
        return
    if node not in visited:
        print( node)
        visited.add(node)
        for i in graph[node]:
            dfs(i,visited,graph)

visited=set()
graph={}
add_node("a")
add_node("b")
add_node("c")
add_node("d")
add_node("e")

add_edge("a","b")
add_edge("b","c")
add_edge("a","c")
add_edge("a","d")
add_edge("b","d")
add_edge("c","d")
add_edge("e","d")
print(graph)
dfs("a",visited,graph)