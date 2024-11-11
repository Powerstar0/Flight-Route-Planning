import csv 
import networkx as nx
import folium
from folium import plugins
from Airport_reading import get_coordinates
def map_creation(G):

    # Create the map centered on a general location, e.g., USA
    m = folium.Map(location=[39.8283, -98.5795], zoom_start=4)

    # Define the coordinates for each airport (make sure these are populated dynamically as needed)
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
        else:
            print(f"Skipping node {node} due to missing coordinates.")

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
        else:
            print(f"Skipping edge between {start} and {end} due to missing coordinates.")


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