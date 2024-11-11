import csv 
import networkx as nx
import folium
from folium import plugins
from geopy.distance import geodesic

airport_coords = {}

# Load OpenFlights data
def extract():
    with open('airports.dat', mode='r', encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            # Extract IATA code, latitude, and longitude
            airport_id = row[4]  # Adjust index as needed based on column order in file
            latitude = float(row[6])
            longitude = float(row[7])
            airport_coords[airport_id] = (latitude, longitude)

# Function to retrieve coordinates
def get_coordinates(airport_id):
    return airport_coords.get(airport_id, None)


# Add edges (node_from, node_to, weight)
def route_extract(g,G):
    with open("routes.dat","r") as file:
        csvFile = csv.reader(file)
        for line in csvFile:
            """
            Sample: BA,1355,SIN,3316,LHR,507,,0,744 777
            Airline	2-letter (IATA) or 3-letter (ICAO) code of the airline.
            Airline ID	Unique OpenFlights identifier for airline (see Airline).
            Source airport	3-letter (IATA) or 4-letter (ICAO) code of the source airport.
            Source airport ID	Unique OpenFlights identifier for source airport (see Airport)
            Destination airport	3-letter (IATA) or 4-letter (ICAO) code of the destination airport.
            Destination airport ID	Unique OpenFlights identifier for destination airport (see Airport)
            Codeshare	"Y" if this flight is a codeshare (that is, not operated by Airline, but another carrier), empty otherwise.
            Stops	Number of stops on this flight ("0" for direct)
            Equipment	3-letter codes for plane type(s) generally used on this flight, separated by spaces
            """
            # Extract source and destination
            source = line[2]
            destination = line[4]
            point1 = get_coordinates(source)
            point2 = get_coordinates(destination)
            distance = round(geodesic(point1, point2).kilometers)
            #print(str(source) + " " + str(desination) + " " + str(distance) + " km")
            g.add_edge(source, destination, distance)
            # Ensure that the source and destination nodes are added to the graph
            if source not in G:
                G.add_node(source)
            if destination not in G:
                G.add_node(destination)
            G.add_edge(source, destination, distance=distance)
