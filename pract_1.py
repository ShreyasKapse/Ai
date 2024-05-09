graph = {
'5' : ['3','7'],
'3' : ['2','4'],
'7' : ['9'] ,
'2' : [] ,
'4' : ['8'],
'9' : [],
'8' : []
}
visited = []
queue = []
def bfs (visited,graph,node) :
    visited.append(node)
    queue.append(node)
    while queue :
        m = queue.pop(0)
        print (m,end=" ")
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

print("bfs")
bfs(visited,graph,'5')




# DFS


graph = {
'7': ['5', '9'],
'5' : ['2', '4'],
'9' : ['8','11'],
'2' : [],
'4' : [],
'8' : [],
'11': []
}

visited = set()
def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
print("Following is the Depth-First Search")
dfs(visited, graph, '7')
