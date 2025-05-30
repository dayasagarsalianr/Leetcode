from heapq import heappop, heappush
from collections import defaultdict
from math import inf
from typing import List

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        # Define a Dijkstra's algorithm function to find shortest paths from a starting node
        def dijkstra(start_node):
            # Initialize distance array with infinity values
            distances = [inf] * num_nodes
            # Distance to the start node is 0
            distances[start_node] = 0
            # Priority queue for the Dijkstra algorithm, containing tuples of (distance, node)
            priority_queue = [(0, start_node)]
          
            # Process the queue until it is empty
            while priority_queue:
                # Pop the node with the smallest distance from the queue
                current_distance, current_node = heappop(priority_queue)
                # Iterate over all adjacent nodes
                for neighbor in graph[current_node]:
                    # If a shorter path to the neighbor is found, update the distance and add it to the queue
                    if distances[neighbor] > current_distance + 1:
                        distances[neighbor] = current_distance + 1
                        heappush(priority_queue, (distances[neighbor], neighbor))
          
            return distances

        # Construct the graph using a default dictionary to hold adjacency lists
        graph = defaultdict(list)
        for i, neighbor in enumerate(edges):
            if neighbor != -1:
                graph[i].append(neighbor)
      
        # Count the number of nodes
        num_nodes = len(edges)
      
        # Run Dijkstra's algorithm from both given nodes
        distances_from_node1 = dijkstra(node1)
        distances_from_node2 = dijkstra(node2)
      
        # Initialize the answer and the smallest maximum distance found
        closest_meeting_node = -1
        smallest_max_distance = inf
      
        # Iterate over each node to find the optimal meeting node
        for i, (distance_node1, distance_node2) in enumerate(zip(distances_from_node1, distances_from_node2)):
            # Compute the larger of the two distances
            current_max_distance = max(distance_node1, distance_node2)
          
            # If this node has a smaller or equal max distance, it's a candidate
            if current_max_distance < smallest_max_distance:
                # Update the closest meeting node and the smallest maximum distance
                smallest_max_distance = current_max_distance
                closest_meeting_node = i
      
        # Return the index of the closest meeting node (or -1 if not found)
        return closest_meeting_node