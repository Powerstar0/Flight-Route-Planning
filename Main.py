import csv 
import networkx as nx
import folium
from folium import plugins
from Graph import Graph
from Airport_reading import extract
from Airport_reading import route_extract
from Graph import map_create
from Graph import dijkstra
from Graph import find_unreachable_airports

# Create the graph with NetworkX (optional for further graph manipulation)
G = nx.DiGraph()

# Create a new graph
g = Graph()

extract()
route_extract(g,G)
map_create(G)

print("Map Generated")
while True:
    print("""
Options:
1. Calculate the shortest path between two airports
2. Airports that have the most and incoming and outgoing flights
3. Unreachable airports from your hub
4. Quit
                """)
    userinput = input()
    if (userinput == "1"):
        starting_airport = input("What is the starting hub? (3 letter IATA code): ")
        ending_airport = input("What's your ending hub? (3 letter IATA code): ")
        # Run Dijkstra's algorithm starting from node
        distances = dijkstra(g, starting_airport)

        # Output the shortest distances from "LAX" to all other nodes, sorted by distance
        print(f"\nShortest distances from airport {starting_airport}:")

        # Sort the distances by value (distance) and print the results
        for node, distance in sorted(distances.items(), key=lambda item: item[1]):
            if node == ending_airport:
                print(f"{node}: {distance} km")
                break
    elif (userinput == "2"):
        # To print the top 5 nodes with the most outgoing edges
        print("Top 5 nodes with the most outgoing flights:")
        for node, count in g.nodes_with_most_outgoing():
            print(f"Airport: {node}, Outgoing flights: {count}")

        # To print the top 5 nodes with the most incoming edges
        print("\nTop 5 nodes with the most incoming flights:")
        for node, count in g.nodes_with_most_incoming():
            print(f"Airport: {node}, Incoming flights: {count}")
    elif (userinput == "3"):
        starting_airport = input("What is the starting hub? (3 letter IATA code): ")
        unreachable_airports = find_unreachable_airports(g, starting_airport)
        print(f"Airports that cannot be reached from {starting_airport}: {unreachable_airports}")
    elif (userinput == "q"):
        break
    else:
        print("Invalid Input")





