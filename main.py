def bfs_helper(city, adj_dict, distance_threshold, n):
    previous = [None for i in range(n)]
    visited = set()
    distance = [float('inf') for i in range(n)]

    import heapq
    priority_queue = []

    heapq.heappush(priority_queue, city)

    # print(priority_queue)

    distance[city] = 0

    while priority_queue:
        current_city = heapq.heappop(priority_queue)

        # print('current city is now: ', current_city)

        visited.add(current_city)

        neighbors = adj_dict[current_city]

        for neighbor, weight in neighbors:
            if neighbor not in visited:
                calculated_weight = distance[current_city] + weight

                if calculated_weight <= distance_threshold:
                    # update distance[neighbor] = calculated_weight
                    # update previous[neighbor] = current
                    # add this neighbor to visited
                    distance[neighbor] = calculated_weight
                    previous[neighbor] = current_city

                # visited.add(neighbor)
                heapq.heappush(priority_queue, neighbor)

    # print('distance: ', distance)
    # print('visited: ', visited)
    # print('previous: ', previous)

    result = 0

    for d in distance:
        if d != 0 and d != float('inf'):
            result +=1

    # print(result)
    return result             


# city = 3
# n = 4
# # edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
# adj_dict = {0: [(1, 3)], 1: [(0, 3), (2, 1), (3, 4)], 2: [(1, 1), (3, 1)], 3: [(1, 4), (2, 1)]}
# distance_threshold = 4

# bfs_helper(city, adj_dict, distance_threshold, n)


city = 2
n = 5
# edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]]
distance_threshold = 2
adj_dict = {0: [(1, 2), (4, 8)], 1: [(0, 2), (2, 3), (4, 2)], 4: [(0, 8), (1, 2), (3, 1)], 2: [(1, 3), (3, 1)], 3: [(2, 1), (4, 1)]}
bfs_helper(city, adj_dict, distance_threshold, n)

def find_the_city(n, edges, distance_threshold):
    # pass

    # create variable previous that tracks the previous city from the start city
    # vistied to track all visited cities
    # distance from the start city

    # adj_dict , key will be the start city, values lists of tuples (end city, weight)

    # variable cities - dictionaryu(key city, value number of neighbors)

    # loop all cities in adj_dict:
        # for each city call helpfuntion
        # helpfunction that gives a number of neighbors from the current cities that within the threshold
            # create variable previous that tracks the previous city from the start city [None]
            # vistied to track all visited cities 
            # distance from the start city , list of n size , set inifity 

            # initilize priority queue
            #  add the current city to the queue
            # set distance of current city as 0


            # while queue:
                # pop the fisrt one of queue and add it visited
                # find all neighbors of current nodes
                    # if neibhbor is not visited:
                        # calculate the weight = distance[current] + weight of neighbor
                        # if calculated weight < distance[neighbor] and calcualte weight < threshold:
                            # update distance[neighbor] = calculated_weight
                            # update previous[neighbor] = current
                        # add this neighbor to visited
                        # add this to the queue

            # return the distance that is not inifity or zero




    # add the following to cities dict: add the city and neighbors to 
    # find the minim of the cities
    # if there is no tie:
        # return the city
    # if there if tie:
        # return the largest city

    adj_dict = {}

    for start, end, weight in edges:
        if start not in adj_dict:
            adj_dict[start] = [(end, weight)]
        else:
            adj_dict[start].append((end, weight))

        if end not in adj_dict:
            adj_dict[end] = [(start, weight)]
        else:
            adj_dict[end].append((start, weight))

    # print(adj_dict)

    cities = {}

    for i in range(n):
        cities[i] = 0
    # print(cities)

    for city in cities:
        city_neighbors = bfs_helper(city, adj_dict, distance_threshold, n)

        cities[city] = city_neighbors
    
    # print(cities)

    min_cities = [None]

    min_neighbors = float('inf')
    min_city = None

    for city, neighbors in cities.items():
        if neighbors < min_neighbors:
            min_city = city
            min_neighbors = neighbors
            min_cities = [min_city]
        
        elif neighbors == min_neighbors:
            min_cities.append(city)

    # print(min_cities)

    if len(min_cities) == 1:
        return min_cities[0]
    elif len(min_cities) > 1:
        sorted_min_cities = sorted(min_cities)
        return sorted_min_cities[-1]





# n = 4
# edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
# distance_threshold = 4

# find_the_city(n, edges, distance_threshold)

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
