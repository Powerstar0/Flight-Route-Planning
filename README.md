# Flight Route Planning

With Permission and Assistance of Duy Lam dplb6c@umkc.edu

Authors: Johnny Diep jd53q@umkc.edu, Steven Pham sdprg3@umkc.edu, and Duy Lam (Duy Lam is currently in another Hack-a-roo group but has given permission for us to use this project for our own)

## Introduction

This project investigates airport traffic data from 2014 to provide a comprehensive view of global connectivity among airports. By examining flight routes and worldwide airport networks, the project builds a detailed database that reveals the structure and dynamics of global air traffic. This database identifies key hubs, high-traffic routes, and regional connectivity, offering insights into the busiest and most critical nodes that link different parts of the world. The 2014 snapshot also serves as a valuable historical benchmark, helping to inform future studies on how air traffic networks evolve over time and aiding in strategic planning for infrastructure and resources within the aviation industry. To complement the data analysis, the project generates a visual network map, displaying each airport as a node and each flight route as an edge. This graphical representation enhances our understanding of global air traffic, emphasizing dense traffic regions and the significance of major hubs in facilitating international connectivity.

## Objectives

Build a Comprehensive Database: Compile 2014 airport and flight route data into a structured database, capturing relevant information such as airport locations, traffic volumes, and route connectivity.

Visualize the Airport Network: Create a graphical representation of the airport network, mapping airports as nodes and direct flight routes as edges to highlight connectivity and identify regional and global traffic patterns. Node sizes vary based on connections to other airports.

Enable Route Optimization Analysis: Develop a tool that allows users to find the shortest route between any two selected airports. This feature is designed to facilitate route optimization and help understand direct and indirect connectivity across the global airport network.

Identify Isolated Airports Relative to Major Hubs: Provide a feature to identify unconnected airports relative to a selected hub. This functionality aims to highlight gaps in direct connectivity, offering insights into regional accessibility and potential areas for network improvement.

## Approaches and Data

The dataset for this study, sourced from openflight.org (2014), includes over 65,000 flight routes and coordinates for more than 7,000 airports worldwide. From this data, we constructed a graph where nodes represent airports, and edges represent unique, direct flight routes. By counting and sorting edges, we identified the airports with the highest numbers of incoming and outgoing connections.
Dijkstra's algorithm was applied to determine the shortest paths between airports and to identify any inaccessible airports from each node. Distances were calculated in kilometers by converting latitude and longitude differences, which improves clarity. On the resulting map, node sizes reflect the number of connections each airport has, with larger nodes representing more interconnected hubs in the network. An HTML file listing all airports and routes is also automatically generated.

## Models

For the full interactive model, please open the HTML file. However, here are a few snapshots:

<img width="1123" alt="Screenshot 2024-11-11 at 8 15 31 PM" src="https://github.com/user-attachments/assets/a3d9bbfa-95d1-4610-bb7b-b33bbb78e36f">

<img width="1677" alt="Screenshot 2024-11-11 at 7 07 28 PM" src="https://github.com/user-attachments/assets/919459b5-ab19-4c2c-84ec-e2493319a353">

<img width="179" alt="Screenshot 2024-11-11 at 8 25 04 PM" src="https://github.com/user-attachments/assets/2ec6d9b7-c592-4eb7-b923-b679f0482023">

Additionally, when running the program you can:

1) Find the shortest distance between two airports
  
<img width="343" alt="Screenshot 2024-11-11 at 8 31 19 PM" src="https://github.com/user-attachments/assets/6b083735-38dd-4235-a5c0-e705bd370bd5">


2) Find the top 5 airports with the most outgoing and incoming flights

<img width="325" alt="Screenshot 2024-11-11 at 8 31 30 PM" src="https://github.com/user-attachments/assets/dff78b18-ed38-482f-a3b7-4dbe187b720b">

3) Find unreachable airports from your starting hub

<img width="323" alt="Screenshot 2024-11-11 at 8 31 34 PM" src="https://github.com/user-attachments/assets/6c313307-e635-4ba0-bf1c-4a25358d6f49">

## Findings

This project offers an innovative approach to visualizing and analyzing airport networks using an interactive HTML map. By representing airports as nodes and traffic as lines, the project makes it easy to understand complex connections and identify key patterns in air travel. The features of calculating the shortest route between airports, identifying unconnected nodes, and analyzing the most outgoing traffic provide valuable insights for a variety of users, from travelers to transportation planners. 

The shortest route calculation feature is significant for optimizing travel plans, helping users find the most efficient connections between airports. The unconnected nodes tool highlights potential gaps in the network, which could inform decisions for infrastructure expansion or route development. Additionally, the most outgoing traffic analysis offers a deeper understanding of airport utilization, allowing airport authorities and airlines to better manage resources and operations at busy hubs. 

The innovation lies in how these features are integrated into an interactive map that users can explore in real-time, making the data more accessible and actionable. The project’s ability to turn complex airport network data into an interactive, user-friendly tool has the potential to improve decision-making and efficiency in the airline industry.

In all, this project successfully generated an HTML map to represent a network of airports as nodes and their traffic connections as lines. The key functionality provided includes a route-finding feature to determine the shortest path between two airports, a tool to identify unconnected nodes from a specific airport, and a feature to shows airports with the most outgoing and incoming flights. These features enable users to analyze the network's structure, identify isolated airports, and gain insights into traffic patterns. 

## Future Work

Future enhancements to this project include integrating live data, utilizing the Google Maps API, and expanding program features. Planned features could estimate costs based on real-time rates, predict fuel usage, account for different airlines, and incorporate layovers. Additionally, machine learning models could be implemented to predict future expansions, flight routes, and pricing trends. Enhancing the front-end and user interface will also make the program more accessible and user-friendly.
 



