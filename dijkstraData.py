'''
Programming assignment 5:

implement the Dijkstra's
algorithm for computing
shortest paths in a graph.

If there is no path,
define its distance as 1000000.

'''

import heapq

def readUndirectedGraph(filename):
    
    adjlist = []
    
    f = open(filename) 
    #lines = open(filename).read().splitlines()
    
    for line in f.readlines():
        
        adjlist.append([])
        data = line.split()
        v = int(data[0])-1
        
        for tpl in data[1:]:
            
            ts, ws = tpl.split(',')
            t = int(ts)-1
            w = int(ws)
            
            adjlist[v].append((t, w))

    f.close()

    return adjlist

def dijkstraShortestPaths(graph, s):
    '''
    Works in O(n^2), since we use
    an array to maintain the priority queue.
    '''
    
    infinity = 1000000

    n = len(graph) 

    weights = [infinity]*n
    weights[s] = 0
    
    pqueue = []
    heapq.heappush(pqueue, (0, 0))
    
    visited = [False]*n
    
    while len(pqueue) > 0:
                
        #v = extract_min(pqueue, weights)
        node = heapq.heappop(pqueue)
        v = node[1]
        visited[v] = True
    
        for inc, w in graph[v]:
            new_weight = weights[v] + w
            if not visited[inc]:
                if weights[inc] > new_weight:
                    weights[inc] = new_weight
                    heapq.heappush(pqueue, (weights[inc], inc))
                
    return weights


def main():
    
    desired = [7,37,59,82,99,115,133,165,188,197]
    
    graph = readUndirectedGraph('dijkstraData.txt')
    weights = dijkstraShortestPaths(graph, 0)
    
    res = []
    for i in desired:
        res.append(str(weights[i-1]))
        
    print(','.join(res))       
    
if __name__ == '__main__':
    main()
    
