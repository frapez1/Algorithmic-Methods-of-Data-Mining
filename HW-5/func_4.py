############
# This file contain the code for the first function "Shortest Route"
#It takes in input:
#   - a node H
#   - A set of nodes p = {p_1, ..., p_n}
#   - One of the following distances function: t(x,y), d(x,y) or network distance 
#     (i.e. consider all edges to have weight equal to 1).
# Implement an algorithm that returns the shortest walk that goes from H to p_n, and 
# that visits the nodes in p.
############


import numpy as np
import networkx as nx
import gzip
from itertools import islice
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from itertools import combinations 
from scipy.spatial import distance
from func_3 import f3
import webbrowser



# path for read files
path = 'C:/Users/franc/Desktop/Data_science/Algorithmic_Methods_of_Data_Mining/ADM_hw5/'


# the three func to built the graphs take as argument a nx.Graph()
# we are going to create the graph with the distance in meters
def d(graph):
    with gzip.open(path + "distance.gz", "r") as f:
        for line in islice(f, 7, None):
            r, s, t  = map(int, line[2:].split())
            graph.add_edge(r, s, weight = t)
    return graph

# we are going to create the graph with the time distance
def t(g):
    with gzip.open(path + "time_travel.gz", "r") as f:
        for line in islice(f, 7, None):
            r, s, t  = map(int, line[2:].split())
            g.add_edge(r, s, weight = t)
    return g

# we are going to create the graph with the network distance
def n(g):
    with gzip.open(path + "distance.gz", "r") as f:
        for line in islice(f, 7, None):
            r, s, t  = map(int, line[2:].split())
            g.add_edge(r, s, weight = 1)
    return g

# we are going to save all the coordinates into a dictionary in this form
'''
coord = {node_1 : (long, lat),
         node_2 : (long, lat),
         .
         .
         .}
'''
def coordinates(coord):
    with gzip.open(path + "coordinates.gz", "r") as f:
        for line in islice(f, 7, None):
            x = line[2:].split()
            r, s, t  = int(x[0]), float(x[1])/10**6, float(x[2])/10**6
            coord[r] = (s, t)
    return coord


# this is the function to find the heuristic solution for this problem
# take as argument a fully connecteg graph where the weights are the eucledian distances
# between the nodes
# to find the best path we use the a kind of Nearest Neighbour Algorithm    
def shortest_path_l_r(dcf_graph, start, end):    
    visited = [start, end]
    tot_dist = 0
    while len(visited) < len(dcf_graph):
        # this is for one side
        min_dist = np.inf
        near = 0
        for k,v in dcf_graph[visited[len(visited)//2 - 1]].items():
            if k not in visited:
                if v < min_dist:
                    min_dist = v
                    near = k
        visited.insert(len(visited)//2, near)
        tot_dist += min_dist
        # this is for the other
        min_dist = np.inf
        near = 0
        for k,v in dcf_graph[visited[len(visited)//2 + 1]].items():
            if k not in visited:
                if v < min_dist:
                    min_dist = v
                    near = k
        # at the end if we have a even numbaer of vertex
        if near != 0:
            visited.insert(len(visited)//2 + 1, near)
            tot_dist += min_dist
    return visited, tot_dist

# we built the fully connected graph as a dictionary in this way
'''
dictionary = {node_1 : {node_i : weight,
                        node_j : weight,
                        node_k : weight},
              node_2 : {node_l : weight,
                        node_m : weight,
                        node_n : weight}}
             }
'''
def fully_connected_graph(dcf_graph, comb, coord):
    for vert in comb:
        r, s = vert
        t = distance.euclidean(coord[r], coord[s])
        if r not in dcf_graph:
            dcf_graph[r] = {s: t}
        else:
            dcf_graph[r][s] = t
        if s not in dcf_graph:
            dcf_graph[s] = {r: t}
        else:
            dcf_graph[s][r] = t
    return dcf_graph

# choose the best path between the two that we are going to evaluate
def best_order(dcf_graph, rand_po):    
    visited_1, dist_1 = shortest_path_l_r(dcf_graph, rand_po[0], rand_po[-1])
    visited_2, dist_2 = shortest_path_l_r(dcf_graph, rand_po[-1], rand_po[0])
    if dist_1 < dist_2:
        visited = visited_1
    else:
        visited = visited_2[::-1]
    return visited
        
# building list of nodes to visit
def nodes_between_start_end(graph, visited):  
    Nodes = []
    for i in range(len(visited)-1):
        Nodes += f3(graph, visited[i], visited[i+1]) 
    return Nodes

# the visualization part used for func_3 and func_4
def visualization_4(visited, Nodes, coord):
    # we import and delet it into the func 
    import folium
    #starting node for center the map
    starting = coord[visited[0]]
    mapit = folium.Map( location=[starting[1], starting[0]], zoom_start = 10 )
    # coordinates of all nodes
    Way = []
    for i in range(len(Nodes)):
        v = coord[Nodes[i]]
        Way.append((v[1], v[0]))
    #street between vertices
    folium.PolyLine(Way, color="gray", weight=2.5).add_to(mapit)
    #plot all the vertices ac circles
    for i in range(len(Way)):
        folium.CircleMarker(Way[i], radius = 3, opacity=0.1 + 0.9*((i+1)/len(Nodes))).add_to(mapit)
    #plot the vertices selected by the user
    for i in range(1,len(visited)-1):
        v = coord[visited[i]]
        folium.Marker((v[1], v[0]), icon=folium.Icon(color='blue', icon='cloud') , radius=8 ).add_to(mapit)
    # change color for starting and ending points
    folium.Marker( Way[0], icon=folium.Icon(color='green', icon='cloud') , radius=8 ).add_to(mapit)
    folium.Marker( Way[-1], icon=folium.Icon(color='red', icon='cloud') , radius=8 ).add_to(mapit)
    # save map
    mapit.save(path + 'map.html')
    # open map on browser
    webbrowser.open(path + 'map.html',new = 2)
    
    
    # We need to removit because otherwise the bulitin map() function doesn't work well
    del folium
 
# the visualization part used for func_1
def visualization_1(Nodes, coord):
    # we import and delet it into the func 
    import folium
    #starting node for center the map
    starting = coord[Nodes[0]]
    mapit = folium.Map( location=[starting[1], starting[0]], zoom_start = 10 )
    #plot the vertices selected by the user
    for i in range(1, len(Nodes)):
        v = coord[Nodes[i]]
        folium.Marker((v[1], v[0]), icon=folium.Icon(color='blue', icon='cloud') , radius=8 ).add_to(mapit)
    v = coord[Nodes[0]]
    folium.Marker((v[1], v[0]), icon=folium.Icon(color='green', icon='cloud') , radius=8 ).add_to(mapit)
    # save map
    mapit.save(path + 'map.html')
    # open map on browser
    webbrowser.open(path + 'map.html',new = 2)
    
    
    # We need to removit because otherwise the bulitin map() function doesn't work well
    del folium
 

