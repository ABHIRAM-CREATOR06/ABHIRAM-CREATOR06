import folium

# Create a base map centered on India
map_india = folium.Map(location=[20.5937, 78.9629], zoom_start=5)

# List of states with their corresponding latitude, longitude, and information
states_info = {
    "Maharashtra": {"coords": [19.7515, 75.7139], "info": "Capital: Mumbai, Known for: Bollywood, Gateway of India"},
    "Kerala": {"coords": [10.8505, 76.2711], "info": "Capital: Thiruvananthapuram, Known for: Backwaters, Ayurveda"},
    "Tamil Nadu": {"coords": [11.1271, 78.6569], "info": "Capital: Chennai, Known for: Temples, Marina Beach"},
    "Karnataka": {"coords": [15.3173, 75.7139], "info": "Capital: Bangalore, Known for: IT Hub, Mysore Palace"},
    "West Bengal": {"coords": [22.9868, 87.8550], "info": "Capital: Kolkata, Known for: Howrah Bridge, Durga Puja"},
    "Rajasthan": {"coords": [27.0238, 74.2179], "info": "Capital: Jaipur, Known for: Forts, Thar Desert"},
    "Punjab": {"coords": [31.1471, 75.3412], "info": "Capital: Chandigarh, Known for: Golden Temple, Bhangra"},
    "Gujarat": {"coords": [22.2587, 71.1924], "info": "Capital: Gandhinagar, Known for: Gir Forest, Sabarmati Ashram"},
    "Uttar Pradesh": {"coords": [26.8467, 80.9462], "info": "Capital: Lucknow, Known for: Taj Mahal, Varanasi Ghats"},
    "Assam": {"coords": [26.2006, 92.9376], "info": "Capital: Dispur, Known for: Tea Gardens, Kaziranga National Park"}
}

# Add markers for each state
for state, data in states_info.items():
    folium.Marker(
        location=data["coords"],
        popup=f"{state}: {data['info']}",
        tooltip=state,
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(map_india)

# Save the map as an HTML file
map_india.save("india_map.html")

print("Map has been created and saved as india_map.html")
