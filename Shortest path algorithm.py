my_graph = {

    'A': [('B', 3), ('C', 2)],
    'B': [('D', 2), ('A', 3)],
    'C': [('D', 1), ('A', 2)],
    'D': [('B', 2), ('C', 1)],
}

def shortest_path(graph,start,target = ''):
    unvisited = list(graph)
    distances = {node: 0 if node == start else float('inf') for node in graph}
    paths = {node: [] for node in graph}
    paths[start].append(start)

    while unvisited:
        current = min(unvisited,key=distances.get)
        for node, distance in graph[current]:
            new_distances = distance + distances[current]
            if new_distances < distances[node]:
                distances[node] = new_distances
                if paths[node] and paths[current][-1]  == node:
                   paths[node] = paths[current][:]
                else:
                    paths[node].extend(paths[current])
                    paths[node].append(current)
        unvisited.remove(current)


    targets_to_print = [target] if target else graph


    for node in targets_to_print:
       if node == start:
          continue
       print(f'\n{start}-{node} distance: {distances[node]} \nPath: {"->".join(paths[node])}')

    return distances, paths


shortest_path(my_graph, 'A')



