############
# This is the Python script which executes the whole system. It has to ask some inputs 
# and provide outputs.
# There is, first of all the possibility to choose the type of distance
############
import numpy as np
import networkx as nx
import gzip
from itertools import islice
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from itertools import combinations 
from scipy.spatial import distance
import func_1 as f_1
import func_3 as f_3
import func_4 as f_4

# %%
# is a list of function for built the graph
built_graph = [f_4.d, f_4.t, f_4.n]

graphs = [built_graph[i](nx.Graph()) for i in range(len(built_graph))]
#save the coordinates
coord = f_4.coordinates({})

# %%
# choose the functionality
while True:
    func = int(input('Hi, you can choose a functionality between 1 and 4, what do you want?  '))
    if func in [1,2,3,4]:
        break
    else:
        print('Try again')
# choose the distance
while True:
    print('Now you can choose the type of distance, just writing the number')
    print('1 - distance in meters') 
    print('2 - time distance')
    print('3 - network distance')
    what = int(input('What do you want?   '))
    if what in [1,2,3]:
        print('\nWe are working on it\n')
        break
    else:
        print('\nTry again \n\n')


#built the graph
graph = graphs[what-1]


if func == 1:
    
    # choose starting point
    while True:
        try:
            start = int(input('Choose the starting vertex   '))
            if start > 1890815 or start < 1:
                print(print('\nPlease enter values ​​between 1 and 1890815\n'))
            else:
                break
        except:
            print('\nPlease enter values ​​between 1 and 1890815\n')
    # choose distance
    while True:
        dist = float(input('Choose the max distance   '))
        try:
            if int(dist) < 0:
                print(print('\nPlease try again\n'))
            else:
                break
        except:
            print('\nPlease try again\n')
    b = {start : {'weight' : 0}} 
    a = list(b.keys())[0]
    c = f_1.f1(graph, b, dist)
    points = list(c)
    points.append(start)
    f_4.visualization_1(points, coord)
    

if func == 2:
    pass

if func == 3:
    while True:
        print('Enter a list of numbers corresponding to the vertex you want to visit.')
        print('Divide the numbers by commas.')
        try:
            points = list(map(int,input('Enter your vertices  ').split(',')))
            if max(points) > 1890815 or min(points) < 1:
                print('\nPlease enter values ​​between 1 and 1890815\n')
            else:
                break
        except:
            print('\nEnter just numbers\n')
    
    try:
        Nodes = f_4.nodes_between_start_end(graph, points)
        f_4.visualization_4(points, Nodes, coord)
    except:
         print("Cannot reach the end from this starting node")
    

if func == 4:
    while True:
        print('We can find the best way')
        print('Enter a list of numbers corresponding to the vertex you want to visit.')
        print('Divide the numbers by commas.')
        print('Put the starting point as first and the ending point at the end')
        try:
            points = list(map(int,input('Enter your vertices  ').split(',')))
            if max(points) > 1890815 or min(points) < 1:
                print('\nPlease enter values ​​between 1 and 1890815\n')
            else:
                break
        except:
            print('\nEnter just numbers\n')
    
    # built a fully connected graph
    comb = list(combinations(points, 2)) 
    dcf_graph = f_4.fully_connected_graph({}, comb, coord)
    try:
        visited = f_4.best_order(dcf_graph, points)
        Nodes = f_4.nodes_between_start_end(graph, visited)
        f_4.visualization_4(visited, Nodes, coord)
    except:
         print("Cannot reach the end from this starting node")
    

