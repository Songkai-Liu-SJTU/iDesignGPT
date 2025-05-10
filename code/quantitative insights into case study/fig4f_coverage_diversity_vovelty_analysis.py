"""
Figure 4f - Coverage, Diversity, and Novelty Analysis (Final Version)
=====================================================================

Author: Songkai Liu @ Shanghai Jiao Tong University
Date: 2024-11-27

This script computes and analyzes:
- Design space coverage based on the Convex Hull area.
- Internal diversity calculated as the average pairwise distances.
- Incremental innovation metrics including average and maximum novelty, 
  derived from cosine similarity against baseline design solutions.

Corresponds to Figure 4f in the manuscript.

Outputs:
--------
- Calculated metrics in CSV format: `adjusted_metrics.csv`
- Uses UMAP for dimensionality reduction.

Dependencies:
--------------
- sentence-transformers
- scikit-learn
- numpy
- pandas
- matplotlib
- scipy
- umap-learn
"""
import warnings
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import PCA
from umap import UMAP
import numpy as np
import os
import pandas as pd
from scipy.spatial import ConvexHull
from sklearn.metrics.pairwise import pairwise_distances
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Polygon

# Ignore unnecessary warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# Load design data
design_data = [
    {
        'method': 'Initial',
        'modules': {
            'Emergency Rescue and Delivery Module': [
                "Adaptive delivery mechanism",
                "Precision drone delivery system",
                "Fault diagnosis and self-repair function"
            ],
            'Rapid Deployment and Efficient Operation Module': [
                "Automatic deployment system",
                "Quick folding design",
                "Modular portable design"
            ],
            'Environmental Adaptation Module': [
                "Real-time environmental data analysis",
                "Multi-sensor fusion system",
                "Adjustable body structure"
            ],
            'Autonomous Navigation and Information Processing Module': [
                "AI decision support system",
                "GPS + IMU dual navigation",
                "Visual recognition and LIDAR combined navigation"
            ],
            'User Interaction Module': [
                "Wearable device control",
                "Touchscreen user interface",
                "Voice control interaction system"
            ],
            'Propulsion System Module': [
                "Efficient battery and motor combination",
                "Hybrid power system",
                "Ultra-high thrust jet propulsion"
            ],
            'Energy Management Module': [
                "Intelligent energy distribution system",
                "Energy recovery mechanism",
                "Solar and battery hybrid management"
            ],
            'Safety System Module': [
                "AI fault prediction system",
                "Self-monitoring and alarm system",
                "Multiple redundancy sensor design"
            ],
            'Material and Structure Module': [
                "Carbon fiber composite material",
                "Self-healing materials",
                "Lightweight metal alloy"
            ],
            'Communication Module': [
                "5G real-time data transmission",
                "Brain-computer interface control",
                "Multi-band communication system"
            ]
        }
    },
    {
        'method': 'Brainstorm',
        'modules': {
            'Emergency Rescue and Delivery Module': [
                "Add fault diagnosis and self-repair function to improve system reliability",
                "Combine data analysis to improve delivery efficiency",
                "Introduce user feedback mechanism to enhance operational experience"
            ],
            'Rapid Deployment and Efficient Operation Module': [
                "Optimize modular design to enhance portability",
                "Emphasize efficiency in quick deployment",
                "Consider lightweight materials in the design"
            ],
            'Environmental Adaptation Module': [
                "Enhance data fusion capabilities for adapting to complex environments",
                "Introduce environmental monitoring feedback to enhance safety"
            ],
            'Autonomous Navigation and Information Processing Module': [
                "Integrate multiple navigation technologies to enhance precision",
                "Introduce deep learning for improved environment recognition",
                "Improve user interface friendliness"
            ],
            'User Interaction Module': [
                "Combine multiple interaction methods to enhance user experience",
                "Introduce adaptive interfaces for different operational scenarios",
                "Add contextual simulation functionality"
            ],
            'Propulsion System Module': [
                "Combine solid-state batteries to improve performance",
                "Explore new propulsion methods to enhance thrust and endurance"
            ],
            'Energy Management Module': [
                "Introduce predictive algorithms to optimize energy management",
                "Consider environmental impacts to enhance sustainability"
            ],
            'Safety System Module': [
                "Add real-time monitoring and intelligent analysis functionality",
                "Emphasize integration of safety systems with materials for stability"
            ],
            'Material and Structure Module': [
                "Develop new polymer composite materials",
                "Incorporate nanotechnology to improve material properties"
            ],
            'Communication Module': [
                "Enhance real-time communication capabilities to improve remote control",
                "Introduce data analysis functionality to optimize communication efficiency"
            ],
            'Data Collection and Analysis Module': [
                "Real-time data recording and analysis",
                "User operation pattern recognition",
                "Data visualization feedback"
            ],
            'Environmental Monitoring and Feedback Module': [
                "Multi-sensor environmental monitoring",
                "Real-time data feedback to the autonomous navigation module",
                "Adjust environmental adaptability"
            ]
        }
    },
    {
        'method': 'Bionic Design',
        'modules': {
            'Emergency Rescue and Delivery Module': [
                "Inspired by self-deploying robot wings: Utilize rapid deployment mechanism and adaptive delivery design to improve emergency rescue efficiency and accuracy"
            ],
            'Rapid Deployment and Efficient Operation Module': [
                "Inspired by ocean plants: Use lightweight and foldable design for quick deployment in complex environments"
            ],
            'Environmental Adaptation Module': [
                "Inspired by microscopic plankton: Optimize shape and material to enhance environmental adaptability and ensure stable operation in diverse environments"
            ],
            'Autonomous Navigation and Information Processing Module': [
                "Inspired by bird wings: Combine dynamic shape-changing navigation technology to improve flexibility and accuracy in autonomous navigation"
            ],
            'User Interaction Module': [
                "Inspired by octopus: Use programmable stretchable surfaces to enable multiple user interaction methods and improve user experience"
            ],
            'Propulsion System Module': [
                "Inspired by dolphins: Optimize streamlined design to reduce resistance during propulsion and improve energy efficiency"
            ],
            'Energy Management Module': [
                "Inspired by plants: Utilize the principle of natural photosynthesis to optimize energy utilization and storage"
            ],
            'Safety System Module': [
                "Inspired by fish: Design flexible protective devices to withstand external impacts and improve safety"
            ],
            'Material and Structure Module': [
                "Inspired by trees: Mimic the growth patterns of trees to optimize material strength and flexibility"
            ],
            'Communication Module': [
                "Inspired by insects: Utilize efficient signal transmission mechanisms to improve communication stability and speed"
            ],
            'Data Collection and Analysis Module': [
                "Inspired by birds: Observe and learn from environmental information to optimize data collection and analysis mechanisms"
            ],
            'Environmental Monitoring and Feedback Module': [
                "Inspired by marine organisms: Use multi-sensor monitoring to track environmental changes and enhance system responsiveness"
            ]
        }
    },
    {
        'method': 'SCAMPER',
        'modules': {
            'Emergency Rescue and Delivery Module': [
                "Substitute: Replace with adaptive delivery mechanism to enhance flexibility"
            ],
            'Rapid Deployment and Efficient Operation Module': [
                "Combine: Combine quick folding design and automatic deployment system"
            ],
            'Environmental Adaptation Module': [
                "Modify: Combine real-time analysis and multi-sensor fusion"
            ],
            'Autonomous Navigation and Information Processing Module': [
                
            ],
            'User Interaction Module': [
                "Substitute: Replace with wearable device control to enhance experience"
            ],
            'Propulsion System Module': [
                "Modify: Combine efficient batteries with hybrid power system"
            ],
            'Energy Management Module': [
                "Combine: Combine intelligent energy distribution and energy recovery"
            ],
            'Safety System Module': [
                "Substitute: Replace with AI fault prediction system to enhance safety"
            ],
            'Material and Structure Module': [
                "Modify: Combine carbon fiber composite material and self-healing materials"
            ],
            'Communication Module': [            ],
            'Data Collection and Analysis Module': [            ],
            'Environmental Monitoring and Feedback Module': [            ]
        }
    },
    {
        'method': 'TRIZ',
        'modules': {
            'Emergency Rescue and Delivery Module': [
                "Use adaptive delivery mechanism to avoid multiple position adjustments"
            ],
            'Rapid Deployment and Efficient Operation Module': [
                "Use modular design to reduce assembly steps"
            ],
            'Environmental Adaptation Module': [
                "Use real-time data analysis to reduce manual adjustments"
            ],
            'Autonomous Navigation and Information Processing Module': [
            ],
            'User Interaction Module': [
                "Use wearable device control to reduce manual operation"
            ],
            'Propulsion System Module': [
                "Use efficient battery and motor combination to reduce energy loss"
            ],
            'Energy Management Module': [
                "Use intelligent energy distribution to reduce energy waste"
            ],
            'Safety System Module': [
                "Use AI fault prediction system to reduce failure rates"
            ],
            'Material and Structure Module': [
                "Use self-healing materials to reduce maintenance costs"
            ],
            'Communication Module': [            ],
            'Data Collection and Analysis Module': [            ],
            'Environmental Monitoring and Feedback Module': [            ]
        }
    }
]

# Load Sentence-BERT model
model_path = '/root/all-MiniLM-L6-v2'
print(f"Loading Sentence-BERT model from {model_path}...")
model = SentenceTransformer(model_path)
print("Model loaded successfully.\n")

# Initialize variables
all_schemes, methods, step_indices, module_set, scheme_to_module = [], [], [], set(), []

# Create output directory
current_dir = os.path.dirname(os.path.abspath(__file__))
adjusted_output_dir = os.path.join(current_dir, 'output_csv_adjusted')
os.makedirs(adjusted_output_dir, exist_ok=True)

# Accumulate design schemes
print("Accumulating schemes step by step...\n")
current_index = 0
for step in design_data:
    method = step['method']
    methods.append(method)
    modules = step['modules']
    for module, schemes in modules.items():
        module_set.add(module)
        for scheme in schemes:
            all_schemes.append(scheme)
            scheme_to_module.append(module)
    step_indices.append((current_index, len(all_schemes)))
    current_index = len(all_schemes)

# Generate embeddings for all schemes
print("Generating embeddings for all schemes...")
embeddings = model.encode(all_schemes)
print("Embeddings generated successfully.\n")

# Dimensionality reduction function
def perform_dimensionality_reduction(embeddings, method='UMAP'):
    if method == 'PCA':
        reducer = PCA(n_components=2)
    elif method == 'UMAP':
        reducer = UMAP(n_components=2, random_state=42)
    else:
        raise ValueError(f"Unsupported dimensionality reduction method: {method}")
    return reducer.fit_transform(embeddings)

# Perform UMAP dimensionality reduction
print("Reducing embeddings dimensionality using UMAP...")
embeddings_2d = perform_dimensionality_reduction(embeddings, method='UMAP')
print("Dimensionality reduction completed.\n")

# Metric calculation function
def calculate_metrics(similarity_matrix, embeddings_2d, step_indices, scheme_to_module, methods, modules):
    results = []
    combined_indices = []

    for i, method in enumerate(methods):
        combined_indices.extend(range(step_indices[i][0], step_indices[i][1]))
        selected_embeddings = embeddings_2d[combined_indices]

        # Coverage
        if len(selected_embeddings) >= 3:
            try:
                hull = ConvexHull(selected_embeddings)
                coverage = hull.volume
            except Exception as e:
                print(f"ConvexHull error for {method}: {e}")
                coverage = 0
        else:
            coverage = 0

        # Diversity (按模块计算平均值)
        diversity_values = []
        for module in modules:
            module_indices = [idx for idx in combined_indices if scheme_to_module[idx] == module]
            if len(module_indices) >= 2:
                module_embeddings = embeddings_2d[module_indices]
                distances = pairwise_distances(module_embeddings)
                diversity_values.append(np.nanmean(distances))
        diversity = np.mean(diversity_values) if diversity_values else 0

        # Innovation Metrics (按模块计算平均值或最大值)
        avg_innovations, max_innovations = [], []
        for module in modules:
            module_indices = [idx for idx in combined_indices if scheme_to_module[idx] == module]
            initial_indices = [idx for idx in range(step_indices[0][0], step_indices[0][1]) if scheme_to_module[idx] == module]
            if module_indices and initial_indices:
                similarities = similarity_matrix[np.ix_(module_indices, initial_indices)]
                avg_innovations.append(1 - np.mean(similarities))
                max_innovations.append(1 - np.min(similarities))
        avg_innovation = np.mean(avg_innovations) if avg_innovations else 0
        max_innovation = np.max(max_innovations) if max_innovations else 0

        # Save results
        results.append({
            "Method Combination": " + ".join(methods[:i + 1]),
            "Coverage": coverage,
            "Diversity": diversity,
            "Avg Innovation": avg_innovation,
            "Max Innovation": max_innovation,
        })
    return pd.DataFrame(results)

# Compute cosine similarity matrix
print("Computing cosine similarity matrix...")
similarity_matrix = cosine_similarity(embeddings)
print("Cosine similarity matrix computed.\n")

# Calculate all metrics
print("Calculating metrics...")
modules = list(module_set)
metrics = calculate_metrics(similarity_matrix, embeddings_2d, step_indices, scheme_to_module, methods, modules)
metrics.to_csv(os.path.join(adjusted_output_dir, 'adjusted_metrics.csv'), index=False)
print(f"Metrics saved to {adjusted_output_dir}/adjusted_metrics.csv\n")

print("All analyses completed successfully.")
