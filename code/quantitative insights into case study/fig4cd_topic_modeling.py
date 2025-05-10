"""
Figure 4c-d - Topic Modeling and Intertopic Distance Visualization
=================================================================

Author: Songkai Liu @ Shanghai Jiao Tong University
Date: 2024-11-25

This script performs topic modeling using Latent Dirichlet Allocation (LDA) 
on search queries and visualizes:
- Top 5 keywords for each topic (Figure 4c).
- Intertopic Distance Map using PCA (Figure 4d).

Usage:
------
- Run the script directly. Outputs include:
  - Topic keywords CSV: `Topic_Keywords.csv`
  - Top keywords bar chart: `Topic_Top_Keywords.png`
  - PyLDAvis interactive visualization: `LDA_Visualization_Custom.html`
  - Intertopic distance map: `Intertopic_Distance_Map_Customized_Fixed.eps`

Dependencies:
-------------
- numpy
- pandas
- matplotlib
- sklearn
- pyLDAvis
- wordcloud

"""
import numpy as np
import pandas as pd
import pyLDAvis
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation as LDA
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Document data
documents = {
    "Patent": [
        "single-occupant UAV rescue, delivery",
        "autonomous flight emergency response",
        "multirole drone disaster relief"
    ],
    "Web of Science": [
        "UAV for search and rescue",
        "humanitarian aerial delivery",
        "forest rescue",
        "coastal rescue",
        "humanitarian aid",
        "emergency evacuation",
        "disaster response",
        "performance efficiency",
        "payload delivery systems",
        "drone maneuverability"
    ],
    "Red Dot": [
        "Single-occupant aircraft",
        "Emergency response UAV",
        "Humanitarian aid aircraft",
        "Disaster relief drone",
        "Autonomous rescue systems",
        "Multi-environment operation",
        "Payload delivery systems",
        "Versatile aviation technology",
        "Rapid deployment aircraft",
        "Precision maneuvering UAV",
        "Ruggedized aerial vehicles",
        "Agile response aircraft",
        "All-terrain aviation systems",
        "Affordable emergency aircraft",
        "Operational efficiency in aviation",
        "Bad weather drone performance",
        "Obstacle avoidance technology",
        "Autonomy in UAV design",
        "Search and rescue aircraft",
        "Medical emergency drones"
    ]
}

# Step 0: Combine text data
combined_text = {k: " ".join(v) for k, v in documents.items()}
all_text = list(combined_text.values())

# Step 1: Text processing and generate term frequency matrix
vectorizer = CountVectorizer(stop_words='english')
tf_matrix = vectorizer.fit_transform(all_text)
tf_feature_names = vectorizer.get_feature_names_out()

# Step 2: Train LDA model
num_topics = 3
lda_model = LDA(n_components=num_topics, random_state=42)
lda_model.fit(tf_matrix)

# Step 3: Extract top 5 keywords for each topic
top_keywords_per_topic = {}
for topic_idx, topic in enumerate(lda_model.components_):
    top_keywords = [(tf_feature_names[i], topic[i]) for i in topic.argsort()[:-6:-1]]
    top_keywords_per_topic[f"Topic {topic_idx + 1}"] = top_keywords

# Save keywords to CSV file
keyword_data = []
for topic, keywords in top_keywords_per_topic.items():
    for keyword, weight in keywords:
        keyword_data.append({"Topic": topic, "Keyword": keyword, "Weight": weight})

df_keywords = pd.DataFrame(keyword_data)
df_keywords.to_csv("Topic_Keywords.csv", index=False)
print("Top keywords saved to 'Topic_Keywords.csv'.")

# Step 4: Save PyLDAvis visualization as HTML
def sklearn_to_pyldavis(lda_model, tf_matrix, feature_names):
    topic_term_dists = lda_model.components_ / lda_model.components_.sum(axis=1)[:, np.newaxis]
    doc_topic_dists = lda_model.transform(tf_matrix)
    doc_lengths = tf_matrix.sum(axis=1).A1
    term_frequency = tf_matrix.sum(axis=0).A1
    vocab = feature_names
    
    vis_data = pyLDAvis.prepare(
        topic_term_dists=topic_term_dists,
        doc_topic_dists=doc_topic_dists,
        doc_lengths=doc_lengths,
        vocab=vocab,
        term_frequency=term_frequency,
        sort_topics=False
    )
    return vis_data

lda_vis_data = sklearn_to_pyldavis(lda_model, tf_matrix, tf_feature_names)
pyLDAvis.save_html(lda_vis_data, "LDA_Visualization_Custom.html")
print("PyLDAvis visualization saved as 'LDA_Visualization_Custom.html'.")

# Step 5: Save static image of top keywords
fig, ax = plt.subplots(figsize=(10, 8))
for topic_idx, topic in enumerate(lda_model.components_):
    top_keywords = [(tf_feature_names[i], topic[i]) for i in topic.argsort()[:-6:-1]]
    keywords, weights = zip(*top_keywords)
    ax.barh(keywords, weights, label=f"Topic {topic_idx + 1}")

ax.set_xlabel("Weight")
ax.set_ylabel("Keywords")
ax.set_title("Top 5 Keywords Per Topic")
ax.legend()
plt.savefig("Topic_Top_Keywords.png")
print("Static keyword visualization saved as 'Topic_Top_Keywords.png'.")
plt.show()

# Get Intertopic Distance Matrix
intertopic_distances = lda_model.components_ @ lda_model.components_.T
intertopic_distances = intertopic_distances / np.linalg.norm(intertopic_distances, axis=1, keepdims=True)
intertopic_distances_df = pd.DataFrame(intertopic_distances, columns=[f"Topic {i+1}" for i in range(num_topics)],
                                       index=[f"Topic {i+1}" for i in range(num_topics)])

# Get topic marginal distributions
topic_weights = lda_model.components_.sum(axis=1) / lda_model.components_.sum()
topic_weights_df = pd.DataFrame({"Topic": [f"Topic {i+1}" for i in range(num_topics)],
                                  "Weight": topic_weights})

# Save to CSV file
intertopic_distances_df.to_csv("Intertopic_Distances.csv", index=True)
topic_weights_df.to_csv("Topic_Weights.csv", index=False)

print("Exported intertopic distances and topic weights to CSV files.")

# --- Intertopic Distance Visualization ---
import matplotlib.pyplot as plt

# Data extracted from HTML visualization
topics_data = [
    {"x": 0.044156606859340836, "y": -0.030265384700775468, "topics": 1, "Freq": 62.84853910114763},
    {"x": -0.056958336360037054, "y": -0.013603304609825081, "topics": 2, "Freq": 23.734004429946438},
    {"x": 0.012801729500696232, "y": 0.04386868931060056, "topics": 3, "Freq": 13.41745646890594},
]

# Mapping factor from frequency to circle radius
radius_scaling_factor = 0.025  # Adjustments can be made as needed

# Create figure
fig, ax = plt.subplots(figsize=(8, 8))

# Plot circles and annotations
for topic in topics_data:
    x, y = topic["x"], topic["y"]
    radius = (topic["Freq"] / max(t["Freq"] for t in topics_data)) * radius_scaling_factor
    ax.add_artist(plt.Circle((x, y), radius, color="blue", alpha=0.3))
    ax.text(x, y, str(topic["topics"]), ha="center", va="center", fontsize=12, color="black")

# Configure axes
ax.axhline(0, color="gray", linewidth=0.8, zorder=0)  # hor
ax.axvline(0, color="gray", linewidth=0.8, zorder=0)  # ver

# Set axis ranges
ax.set_xlim(-0.08, 0.08)
ax.set_ylim(-0.08, 0.08)

# set ticks
xticks = [-0.08, -0.04, 0, 0.04, 0.08]
yticks = [-0.08, -0.04, 0, 0.04, 0.08]
ax.set_xticks(xticks)
ax.set_yticks(yticks)

# Place tick labels outside to avoid overlapping
for tick in xticks:
    ax.text(tick, -0.01, f"{tick:.2f}", ha="center", va="top", fontsize=10, color="gray")
for tick in yticks:
    ax.text(-0.01, tick, f"{tick:.2f}", ha="right", va="center", fontsize=10, color="gray")

# Remove plot borders
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

# Set title
ax.set_title("Intertopic Distance Map (Customized)", fontsize=16)

# Save as EPS format
plt.savefig("Intertopic_Distance_Map_Customized_Fixed.eps", format="eps", bbox_inches="tight")
plt.show()
