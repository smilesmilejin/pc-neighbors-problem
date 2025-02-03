from collections import defaultdict
from heapq import heappush, heappop

def dijkstras(city, graph, distance_threshold):
    # initialize the queue with the starting city distance set to 0
    queue = [(0, city)]
    # initialize a dictionary to hold distances, also serves as a visited list
    dist = {}

    while queue:
        # pop the highest priority city off the queue
        curr_dist, curr = heappop(queue)

        # if the city has already been visited, move on
        if curr in dist:
            continue

        # if the current city is not the city we are currently finding the neighbors for, set the distance to the city 
        if curr != city:
            dist[curr] = curr_dist

        for neighbor, neighbor_dist in graph[curr]:
            dist_to_neighbor = curr_dist + neighbor_dist
            # don't do anything if the neighbor has been previously visited
            if neighbor in dist:
                continue

            # if the neighboring city is within the distance threshold
            if dist_to_neighbor <= distance_threshold:
                # add the neighbor to the queue to be visited later
                heappush(queue, (dist_to_neighbor, neighbor))

    # return the total number of cities this city could reach in the threshold distance
    return len(dist)

        
def find_the_city(n, edges, distance_threshold):
    # Create an adjacency dictionary to hold the graph
    graph = defaultdict(list)

    # Transform the list of edges to an adjacency dictionary, keeping in mind the graph is undirected
    for start, end, dist in edges:
        graph[start].append((end, dist))
        graph[end].append((start, dist))

    # initially set min cities to infinity
    min_cities = float('inf')
    # set the city with the min number of neighbors to city 0
    city_with_min_neighbors = 0
    
    # iterate through each city
    for city in range(n):
        # find out the number of cities within the threshold for this city
        num_cities_within_threshold = dijkstras(city, graph, distance_threshold)
        # if the number of cities within the threshold is less than or equal to minCities, update minCities and city_with_min_neighbors
        if num_cities_within_threshold <= min_cities:
            min_cities = num_cities_within_threshold
            city_with_min_neighbors = city

    # return the city with the min number of neighbors
    return city_with_min_neighbors


### Test Case #1

r"""
                3             4
        0 ----------- 1 ----------- 3
                       \           /
                        \         /
                         \       /
                        1 \     / 1
                           \   /
                            \ /
                             2
"""
n = 4
edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
distance_threshold = 4

assert find_the_city(n, edges, distance_threshold) == 3

### Test Case #2

r"""
                8             1
        0 ----------- 4 ------------ 3
         \           /             /
          \         /             /
           \       /             /
          2 \     / 2           / 1
             \   /             /
              \ /      3      /
               1 ----------- 2
"""
n = 5
edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]]
distance_threshold = 2

assert find_the_city(n, edges, distance_threshold) == 0

### Test Case #3

r"""
                1             1
        4 ----------- 1 ------------ 3
       /             /             /
      /             /             /
     /             /             /
 10 /             / 10          / 1
   /             /             /
  /             /      1      /
 5             0 ----------- 2
"""
n = 6
edges = [[0,1,10],[0,2,1],[2,3,1],[1,3,1],[1,4,1],[4,5,10]]
distance_threshold = 20

assert find_the_city(n, edges, distance_threshold) == 5

print("All tests passed!")
print("Discuss time & space complexity if time remains.")
