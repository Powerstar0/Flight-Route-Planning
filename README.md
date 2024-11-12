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
