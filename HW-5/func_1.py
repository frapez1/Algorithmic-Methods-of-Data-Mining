############
# This file contain the code for the first function "Find the Neighbours!"
# It takes in input:
#   - a node v
#   - One of the following distances function: t(x,y), d(x,y) or network distance 
#     (i.e. consider all edges to have weight equal to 1).
#   - a distance threshold d
# 
# Implement an algorithm (using proper data structures) that returns the set of nodes 
# at distance <= d from v, corresponding to v’s neighborhood.
###########

import copy


def f1(C,b,dist):
    # Set of all adjacent nodes
    c = set()
    a = list(b.keys())[0]
    # C is the graph, b is the current node and dist is the maximum distance from it
    ric(C,b,dist,c)
    
    
    return c

def ric(C,b,dist,c): #C is the graph
    # Set s to upload the list of nodes whose distance is less than d
    s = set()
    for i in b:
        D = dict(copy.deepcopy(C[i]))
        for k in D:
            # Uploading distance
            D[k]['weight'] += b[i]['weight']
        
            # Checking if the distance from b in less than dist
            if D[k]['weight'] <= dist:
                c.add(k)
                s.add(k)
                
        v = copy.deepcopy(D)        
        for i in D:
            if i not in s:
                del v[i]                
                        
    if len(s) == 0: # If no node is left to check          
        return
    
    else:            
        return ric(C,v, dist,c)