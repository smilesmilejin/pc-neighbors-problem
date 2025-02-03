# Neighbors Problem

Problem belonging to the post-classroom Mock Interview Question Repository.

## Problem Statement

There are `n` cities numbered from 0 to n - 1.

We are given the array `edges` where `edges[i]` holding some value `[from, to, weight]` represents a bidirectional and weighted edge between cities `from` and `to`.

The integer `distance_threshold` is also provided.

Write a function to return the city with the _smallest_ number of cities that are reachable through some path having a total cost of at most `distance_threshold`. If there are multiple such cities, return the city with the _largest_ city number. For example, if city 1 and 3 share the same number of neighbors and both qualify as the city with the smallest number of neighbors within the threshold distance, we would want to return 3, as 3 is larger than 1.

Example:

```
                3             4
        0 ----------- 1 ----------- 3
                       \           /
                        \         /
                         \       /
                        1 \     / 1
                           \   /
                            \ /
                             2

Input: n = 4
       edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
       distance_threshold = 4

Output: 3
```

Starting from each city, we can reach the following other cities while remaining within the distance threshold:

City 0 → City 1, City 2
City 1 → City 0, City 2, City 3
City 2 → City 0, City 1, City 3
City 3 → City 1, City 2

Cities 0 and 3 each have only 2 neighboring cities at `distance_threshold` of 4. Because there is a tie, we return the largest city number, in this case, 3.

## Examples

### Example 1

With a distance threshold of 4, the city with the smallest number of neighbors reachable in the following data is city 3.

```
                3             4
        0 ----------- 1 ----------- 3
                       \           /
                        \         /
                         \       /
                        1 \     / 1
                           \   /
                            \ /
                             2
```

### Example 2

With a distance threshold of 2, the city with the smallest number of neighbors reachable in the following data is city 0.

```
                8             1
        0 ----------- 4 ------------ 3
         \           /             /
          \         /             /
           \       /             /
          2 \     / 2           / 1
             \   /             /
              \ /      3      /
               1 ----------- 2
```

### Example 3

With a distance threshold of 20, the city with the smallest number of neighbors reachable in the following data is city 5.

```
                1             1
        4 ----------- 1 ------------ 3
       /             /             /
      /             /             /
     /             /             /
 10 /             / 10          / 1
   /             /             /
  /             /      1      /
 5             0 ----------- 2
```

## Notes for the Interviewer

### Clarifying Questions

#### Q: What should I return if there is a tie for the minimum amount of neighbors within the threshold?

A: You should return the biggest numbered city. For example if city 1 and city 3 are tied for the minimum amount of neighbors within the threshold, we would want to return 3.

#### Q: How do the edge weights work?

A: Edge weights are stored in the list with the edge, it will be the third index in the list.

#### Q: How do I get all of the neighbors for a particular city?

A: You can find all of the neighbors for a particular city by converting the list of edges to an adjacency dictionary or adjacency list.

### Hints

- If your candidate struggles with an initial algorithm, encourage them to walk through an example and describe how they would do it using only pen and paper and a very small sample graph.

- Another hint is that this problem can be solved using Dijkstra's algorithm. The algorithm will need to be altered to account for the distance threshold. We would not want to travel to a city that is outside of the threshold provided.

- Ask the interviewee about the representation the graph is stored in. Is there a way to translate that representation to one that can be used to perform Dijkstra's algorithm?

## Optional Bonus At-Home Challenges

To be attempted after completing the interview.

- What is the time/space complexity of sample solution?
