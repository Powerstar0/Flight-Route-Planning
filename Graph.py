import csv 
import networkx as nx
import folium
from folium import plugins
import heapq
from Airport_reading import get_coordinates

# Graph Class

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):
        """Adds a directed edge from node u to node v with the given weight."""
        if u not in self.graph:
            self.graph[u] = {}
        self.graph[u][v] = weight
        # Make sure all nodes appear in the graph, even if they have no outgoing edges
        if v not in self.graph:
            self.graph[v] = {}

    def get_neighbors(self, u):
        """Returns the neighbors of node u."""
        return self.graph.get(u, {})
    
    def outgoing_edges_count(self):
        """Returns the number of outgoing edges for each node."""
        outgoing_count = {}
        for u in self.graph:
            outgoing_count[u] = len(self.graph[u])  # Count the neighbors of u
        return outgoing_count

    def incoming_edges_count(self):
        """Returns the number of incoming edges for each node."""
        incoming_count = {node: 0 for node in self.graph}
        # Iterate through the graph to count incoming edges
        for u in self.graph:
            for v in self.graph[u]:
                incoming_count[v] += 1
        return incoming_count

    def nodes_with_most_outgoing(self):
        """Find the top 5 nodes with the most outgoing edges."""
        outgoing_count = self.outgoing_edges_count()
        # Sort nodes by outgoing edge count in descending order, then get the top 5
        top_5_outgoing = sorted(outgoing_count.items(), key=lambda item: item[1], reverse=True)[:5]
        return [(node, count) for node, count in top_5_outgoing]

    def nodes_with_most_incoming(self):
        """Find the top 5 nodes with the most incoming edges."""
        incoming_count = self.incoming_edges_count()
        # Sort nodes by incoming edge count in descending order, then get the top 5
        top_5_incoming = sorted(incoming_count.items(), key=lambda item: item[1], reverse=True)[:5]
        return [(node, count) for node, count in top_5_incoming]

    def __str__(self):
        return str(self.graph)

# dijkstra's algorithm
def dijkstra(graph, start):
    # Initialize the distances dictionary with all nodes set to infinity
    distances = {node: float('inf') for node in graph.graph}
    distances[start] = 0
    
    # Priority queue to store (distance, node)
    pq = [(0, start)]
    
    while pq:
        # Pop the node with the smallest distance
        current_distance, current_node = heapq.heappop(pq)
        
        # If this distance is already greater than the recorded one, skip it
        if current_distance > distances[current_node]:
            continue
        
        # Visit all the neighbors of the current node
        for neighbor, weight in graph.get_neighbors(current_node).items():
            distance = current_distance + weight
            
            # Only consider this new path if it's better
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances

def find_unreachable_airports(graph, start):
    # Run Dijkstra's algorithm to find the shortest paths from the start airport
    distances = dijkstra(graph, start)
    
    # Identify airports that are unreachable (distance is infinity)
    unreachable_airports = [node for node, distance in distances.items() if distance == float('inf')]
    
    return unreachable_airports


def map_create(G):
# Create the map centered on a general location, e.g., USA
    m = folium.Map(location=[39.8283, -98.5795], zoom_start=4)

    # Define the coordinates for each airport (make sure these are populated dynamically as needed)
    # Example coordinates, this could be populated with actual coordinates in your get_coordinates function
    node_coordinates = {
    }

    for node in G.nodes:
        node_coordinates[node] = get_coordinates(node)

    # Add each airport as a circle marker with size based on degree
    for node, coord in node_coordinates.items():
        if coord:  # Only add marker if coordinates are valid
            size = 1 + (G.degree[node] / max(dict(G.degree()).values())) * 30  # Scale factor for size
            folium.CircleMarker(
                location=coord,
                radius=size,
                popup=f"{node} ({G.degree[node]} connections)",
                color="blue",
                fill=True,
                fill_color="blue",
            ).add_to(m)


    # Add edges as lines between airport nodes, with labels displaying distances
    for start, end, data in G.edges(data=True):
        start_coord = node_coordinates.get(start)
        end_coord = node_coordinates.get(end)
        
        # Only add edge if coordinates for both nodes are available
        if start_coord is not None and end_coord is not None:
            distance = data.get("distance", 1)  # Default distance if not provided
            
            folium.PolyLine(
                [start_coord, end_coord],
                color="green",
                weight=0.1,  # Adjust line weight based on distance
                opacity=0.7
            ).add_to(m)

            # Calculate midpoint for label position
            midpoint = [(start_coord[0] + end_coord[0]) / 2, (start_coord[1] + end_coord[1]) / 2]

            folium.Marker(
                location=midpoint,
                icon=folium.DivIcon(
                    html=f'<div style="font-size: 0px; color: black;">{distance} km</div>'
                )
            ).add_to(m)



    # Inject custom JavaScript to change font size based on zoom level
    m.get_root().html.add_child(folium.Element("""
        <script>
        function updateLabelSize() {
            var zoom = map.getZoom();
            var labels = document.querySelectorAll('div[id^="distance-"]');
            labels.forEach(function(label) {
                var fontSize = Math.min(20, 1 + (zoom * 2));  // Adjust font size based on zoom level
                label.style.fontSize = fontSize + "px";
            });
        }

        // Update label sizes when zoom level changes
        map.on('zoomend', updateLabelSize);

        // Initial update of label sizes
        updateLabelSize();
        </script>
    """))

    # Save the map to an HTML file
    m.save("folium_airport_graph.html")