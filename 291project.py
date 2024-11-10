from IPython.display import display, HTML

# Read the HTML file content
with open("C:/Users/Johnny/CS291-Project/map_with_airports_edges_with_labels.html", "r") as file:
    html_content = file.read()

# Display the HTML content directly
display(HTML(html_content))
