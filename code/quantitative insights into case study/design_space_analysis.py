"""
Design Space Analysis and Novelty Evaluation Script
==================================================

This script supports the analysis and visualization of design spaces and novelty metrics 
for conceptual engineering designs, as presented in the paper submitted to *Nature Communications*.

Features:
---------
- Generate semantic embeddings for design solutions using Sentence-BERT.
- Calculate design novelty based on cosine similarity.
- Visualize design space coverage using PCA and Convex Hull plots.
- Compute coverage area and track design space expansion over iterative design methods.
- Output visualizations corresponding to Figure 4e and 4f in the manuscript.

Usage:
------
1. Ensure Sentence-BERT is available at the specified `model_path`.
2. Run the script to automatically generate:
   - Novelty score plot: `output_plots/novelty_scores.png`
   - Design space coverage plot: `output_plots/design_space_coverage.png`
   - Design space area plot: `output_plots/design_space_areas.png`

Dependencies:
-------------
- sentence-transformers
- scikit-learn
- numpy
- matplotlib
- scipy

Author: Songkai Liu @ Shanghai Jiao Tong University
Date: 2024-09-24

"""

import warnings
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import PCA
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull
import os

# Suppress FutureWarnings for cleaner output
warnings.simplefilter(action='ignore', category=FutureWarning)

# Design data definition for multiple design methods and modules
design_data = [
    # Initial design concepts
    {
        'method': 'Initial',
        'modules': {
            'Electrical Energy Receiving and Transmission Module': [
                "Efficient wire transmission (e.g., superconducting materials)",
                "Wireless power transmission (e.g., microwave)",
                "Laser transmission system"
            ],
            'Energy Storage Module': [
                "Supercapacitor energy storage",
                "Lithium-ion battery storage",
                "Solid-state battery storage"
            ],
            'Environmental and System Monitoring Module': [
                "Sensor network monitoring",
                "Fiber optic sensor system",
                "Micro-electro-mechanical systems (MEMS) sensors"
            ],
            'Rapid Deployment Module': [
                "Foldable module design",
                "Inflatable structure design",
                "Self-assembly module"
            ],
            'Safety and Redundancy Module': [
                "Redundant circuit design",
                "Mechanical redundancy system",
                "Software redundancy system"
            ],
            'Load Interface Module': [
                "Standardized interface design",
                "Adaptive interface",
                "Contactless interface"
            ]
        }
    },
    # Additional design methods omitted for brevity, but should be included in full code
]

# Load Sentence-BERT model
model_path = '/root/all-MiniLM-L6-v2'
print(f"Loading Sentence-BERT model from {model_path}...")
model = SentenceTransformer(model_path)
print("Model loaded successfully.\n")

# Initialize variables for design schemes and steps
all_schemes = []
scheme_steps = []
methods = []
step_indices = []

# Create output directory for saving plots
output_dir = 'output_plots'
os.makedirs(output_dir, exist_ok=True)

# Accumulate schemes from each design method
print("Accumulating schemes step by step...\n")
current_index = 0
for step in design_data:
    method = step['method']
    methods.append(method)
    print(f"Processing method: {method}")
    
    added_schemes = []
    modules = step['modules']
    for module, schemes in modules.items():
        for scheme in schemes:
            combined_scheme = f'{module}: {scheme}'
            all_schemes.append(combined_scheme)
            added_schemes.append(combined_scheme)
            print(f"  Added scheme: {combined_scheme}")
    
    step_indices.append((current_index, len(all_schemes)))
    current_index = len(all_schemes)
    print(f"  Total schemes after this step: {len(all_schemes)}\n")

# Generate embeddings using Sentence-BERT
print("Generating embeddings for all schemes...")
embeddings = model.encode(all_schemes)
print("Embeddings generated successfully.\n")

# Calculate cosine similarity matrix
print("Calculating cosine similarity matrix...")
similarity_matrix = cosine_similarity(embeddings)
print("Cosine similarity matrix calculated.\n")

def calculate_novelty(similarity_matrix, step_indices):
    """Calculate novelty scores for each design step."""
    novelty_scores = []
    for i, (start, end) in enumerate(step_indices):
        if i == 0:
            novelty_scores.append(0)
            print(f"Step {i+1} ({methods[i]}): Initial step, novelty score set to 0.")
            continue
        new_indices = range(start, end)
        prev_indices = range(0, start)
        if len(prev_indices) == 0:
            avg_similarity = 0
        else:
            avg_similarity = np.mean(similarity_matrix[np.ix_(new_indices, prev_indices)])
        novelty = 1 - avg_similarity
        novelty_scores.append(novelty)
        print(f"Step {i+1} ({methods[i]}): Novelty Score = {novelty:.4f}")
    return novelty_scores

print("Calculating novelty scores for each step...")
novelty_scores = calculate_novelty(similarity_matrix, step_indices)
print(f"\nNovelty Scores per step: {novelty_scores}\n")

# Plot novelty scores over design methods
print("Plotting Novelty Scores...")
plt.figure(figsize=(10, 6))
steps = list(range(1, len(novelty_scores) + 1))
plt.plot(steps, novelty_scores, marker='o', linestyle='-', color='b')
for i, txt in enumerate(novelty_scores):
    plt.annotate(f"{txt:.2f}", (steps[i], novelty_scores[i]), textcoords="offset points", xytext=(0,10), ha='center')
plt.title('Novelty Score Over Design Method Iterations')
plt.xlabel('Design Method Iterations')
plt.ylabel('Novelty Score (1 - Average Similarity)')
plt.xticks(steps, methods, rotation=45)
plt.grid(True)
plt.tight_layout()
novelty_plot_path = os.path.join(output_dir, 'novelty_scores.png')
plt.savefig(novelty_plot_path)
print(f"Novelty scores plot saved as {novelty_plot_path}.\n")
plt.close()
