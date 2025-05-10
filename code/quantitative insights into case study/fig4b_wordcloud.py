"""
Figure 4b - Word Cloud Visualization of Search Queries
=====================================================

Author: Songkai Liu @ Shanghai Jiao Tong University
Date: 2024-11-22

This script generates a high-resolution word cloud visualization for 
search queries collected during the information-gathering phase, 
highlighting key domains such as UAV and emergency systems.

Usage:
------
- Run the script directly. The output word cloud image will be saved as:
  `Red_Dot_keywords_wordcloud_high_res.png`

Dependencies:
-------------
- matplotlib
- wordcloud

"""
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from matplotlib.colors import LinearSegmentedColormap

# Define a custom colormap
colors = [
    "#09170A",  "#5B4245", "#5E4FA2", "#1B9729", "#3E83A6", 
    "#5491A6", "#518ADC", "#92895E", "#ED6E46", "#D46F84", 
    "#B0A0AD", "#F4C962"
]
custom_cmap = LinearSegmentedColormap.from_list("custom_colormap", colors, N=256)

# Data preparation (Red Dot dataset)
red_dot_keywords = [
    "Single-occupant aircraft", "Emergency response UAV", "Humanitarian aid aircraft",
    "Disaster relief drone", "Autonomous rescue systems", "Multi-environment operation",
    "Payload delivery systems", "Versatile aviation technology", "Rapid deployment aircraft",
    "Precision maneuvering UAV", "Ruggedized aerial vehicles", "Agile response aircraft",
    "All-terrain aviation systems", "Affordable emergency aircraft", 
    "Operational efficiency in aviation", "Bad weather drone performance",
    "Obstacle avoidance technology", "Autonomy in UAV design", "Search and rescue aircraft",
    "Medical emergency drones"
]

# Create the word cloud
wordcloud = WordCloud(
    scale=32,
    width=480,   
    height=180,  
    background_color="white",
    colormap=custom_cmap,
    contour_color='black',  
).generate(" ".join(red_dot_keywords))

# Save as high-resolution PNG image
png_filename = "Red_Dot_keywords_wordcloud_high_res.png"
plt.figure(figsize=(24, 9), dpi=1200)  # 24x9 inch, 1200 DPI
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.tight_layout()
plt.savefig(png_filename, format="png", bbox_inches="tight")

print(f"Word cloud has been saved as a high-resolution PNG file:{png_filename}")
