
def f3(graph, startnode, endnode):
    # Shortest paths from startnode
    shortest_paths = {startnode: (None, 0)}
    # Initial node
    current_node = startnode
    # Set of visited nodes, which we can forget of during our search
    visited_nodes = set()
    
    while current_node != endnode:
        # Adding visited nodes
        visited_nodes.add(current_node)
        # All adjacent nodes from our current node
        destinations = list(graph[current_node])
        # Uploading the path weight to current node in shortest_paths
        weight_to_current_node = shortest_paths[current_node][1]

        for next_node in destinations:
            # Adding the edges weight to the path to our current node
            weight = graph[current_node][next_node]['weight'] + weight_to_current_node
            if next_node not in shortest_paths:
                # Uploading shortest_path with new node and relative distance from current node
                shortest_paths[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    # Uploading weight to start node with the lowest weight possible
                    shortest_paths[next_node] = (current_node, weight)
        # Choosing the new node
        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited_nodes}
        if not next_destinations:
            # If node is unreachable
            return print("Cannot reach {} from {} as starting node".format(endnode, startnode))
        # Choosing next node by lowest weight
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])
    
    # Creating the path
    path = []
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        current_node = next_node
    # Reverse path
    path = path[::-1]
    return path

