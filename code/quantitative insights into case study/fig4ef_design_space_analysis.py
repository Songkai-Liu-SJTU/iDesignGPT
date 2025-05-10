"""
Design Space Analysis and Novelty Evaluation Script 
=====================================================================

Author: Songkai Liu @ Shanghai Jiao Tong University
Date: 2024-09-24

This script supports the advanced analysis and visualization of design spaces 
and novelty metrics for conceptual engineering designs.

Features:
---------
- Generate semantic embeddings for design solutions using Sentence-BERT.
- Calculate design novelty based on cosine similarity, including both 
  average and maximum novelty scores.
- Compute design space coverage using Convex Hull area.
- Analyze internal diversity using average pairwise cosine distance.
- Visualize design space coverage using PCA, t-SNE, and UMAP.
- Output visualizations corresponding to Figure 4e and 4f in the manuscript.

Usage:
------
1. Ensure Sentence-BERT is available at the specified `model_path`.
2. Run the script to automatically generate:
   - Novelty score plot: `output_plots/novelty_scores.png`
   - Design space coverage plots using PCA, t-SNE, and UMAP
   - Design space area plots: `output_plots/design_space_areas.png`
   - Internal diversity plots: `output_plots/internal_diversity.png`

Dependencies:
-------------
- sentence-transformers
- scikit-learn
- numpy
- matplotlib
- scipy
- umap-learn (optional for UMAP visualization)

"""
import warnings
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from umap import UMAP
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull
import os
from sklearn.metrics.pairwise import pairwise_distances

# Ignore FutureWarning to avoid cluttered output
warnings.simplefilter(action='ignore', category=FutureWarning)

# Define design data (only scheme descriptions are in English)
design_data = [
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
    {
        'method': 'Brainstorm',
        'modules': {
            'Electrical Energy Receiving and Transmission Module': [
                "Hybrid transmission scheme (combining superconducting and laser)"
            ],
            'Energy Storage Module': [
                "Hybrid energy storage system (supercapacitor and solid-state battery)"
            ],
            'Environmental and System Monitoring Module': [
                "Adaptive algorithms and edge computing combination"
            ],
            'Rapid Deployment Module': [
                "Coupled module design"
            ],
            'Safety and Redundancy Module': [
                "Intelligent monitoring system to enhance safety"
            ],
            'Load Interface Module': [
                "Standardizing interfaces for rapid integration"
            ]
        }
    },
    {
        'method': 'Bionic Design',
        'modules': {
            'Electrical Energy Receiving and Transmission Module': [
                "Inspired by the golden snail's three-layer shell structure, design materials that effectively disperse and transmit electricity to reduce losses."
            ],
            'Energy Storage Module': [
                "Reference flexible lithium-ion battery design to enhance flexibility and high energy density under extreme conditions."
            ],
            'Environmental and System Monitoring Module': [
                "Inspired by flathead fish's perception system, integrate multiple sensors for more precise environmental monitoring."
            ],
            'Rapid Deployment Module': [
                "Inspired by the snail's movement mechanism, design modules that can self-adjust according to environmental changes."
            ],
            'Safety and Redundancy Module': [
                "Inspired by spider web structures, utilize their strength and flexibility in designing redundancy systems."
            ],
            'Load Interface Module': [
                "Inspired by biological adaptability mechanisms, design interfaces capable of quickly adapting to different loads."
            ],
            # New modules
            'Thermal Management Module': [
                "Thermal insulation materials",
                "Active thermal management system",
                "Phase change materials combined with heat pipe technology"
            ],
            'Environmental Adaptability Module': [
                "Intelligent algorithm to assess environmental changes",
                "Integrated thermal management and radiation-resistant design",
                "Material adaptability assessment"
            ]
        }
    },
    {
        'method': 'SCAMPER',
        'modules': {
            'Electrical Energy Receiving and Transmission Module': [
                "Adapt: Combine superconducting materials and laser technology to develop a multifunctional energy transmission system."
            ],
            'Energy Storage Module': [
                "Modify: Optimize energy management strategies of the storage system to improve efficiency."
            ],
            'Environmental and System Monitoring Module': [
                "Combine: Integrate adaptive algorithms with multi-sensor systems to enhance environmental monitoring capabilities."
            ],
            'Rapid Deployment Module': [
                "Substitute: Introduce fast assembly technology to improve deployment speed."
            ],
            'Safety and Redundancy Module': [
                "Eliminate: Simplify redundancy designs to reduce weight."
            ],
            'Load Interface Module': [
                "Modify: Design adjustable interfaces to enhance compatibility."
            ],
            'Thermal Management Module': [
                "Combine: Integrate active and passive thermal management technologies to improve thermal efficiency."
            ],
            'Environmental Adaptability Module': [
                "Adapt: Introduce intelligent materials to enhance environmental adaptability."
            ]
        }
    },
    {
        'method': 'TRIZ',
        'modules': {
            'Electrical Energy Receiving and Transmission Module': [
                "Implement dynamic adjustment mechanisms to optimize transmission methods under different environmental conditions."
            ],
            'Energy Storage Module': [
                "Design multifunctional storage systems that combine various energy storage functionalities."
            ],
            'Environmental and System Monitoring Module': [
                "Use replaceable sensor modules to achieve flexible monitoring."
            ],
            'Rapid Deployment Module': [
                "Introduce adjustable structures to quickly adapt to different deployment environments."
            ],
            'Safety and Redundancy Module': [
                "Use intelligent monitoring systems to replace some redundancy features, enhancing efficiency."
            ],
            'Load Interface Module': [
                "Use adjustable interfaces to accommodate different loads."
            ],
            'Thermal Management Module': [
                "Dynamically adjust thermal management strategies to improve energy efficiency."
            ],
            'Environmental Adaptability Module': [
                "Use intelligent materials to dynamically adjust to environmental changes."
            ]
        }
    }
]

# Initialize the Sentence-BERT model
model_path = '/root/all-MiniLM-L6-v2'  # Ensure the model path is correct
print(f"Loading Sentence-BERT model from {model_path}...")
model = SentenceTransformer(model_path)
print("Model loaded successfully.\n")

# Initialize variables
all_schemes = []      # Accumulate all schemes
methods = []          # Record the name of each step
step_indices = []     # Record the index range of schemes for each step
module_set = set()    # Record all module names
scheme_to_module = [] # Map each scheme to its module

# Create output directory to save images
output_dir = 'output_plots'
os.makedirs(output_dir, exist_ok=True)

# Stepwise accumulation of schemes
print("Accumulating schemes step by step...\n")
current_index = 0
for step in design_data:
    method = step['method']
    methods.append(method)
    print(f"Processing step: {method}")
    
    modules = step['modules']
    for module, schemes in modules.items():
        module_set.add(module)  # Record module name
        for scheme in schemes:
            all_schemes.append(scheme)      # Only append scheme description
            scheme_to_module.append(module) # Map scheme to its module
            print(f"  Added scheme: {scheme}")
    
    # Record the current step's scheme index range
    step_indices.append((current_index, len(all_schemes)))
    current_index = len(all_schemes)
    print(f"  Total number of schemes after this step: {len(all_schemes)}\n")

# Determine baseline schemes (Initial step's schemes)
initial_schemes = []
initial_modules = design_data[0]['modules']
for module in initial_modules:
    initial_schemes.extend(initial_modules[module])
initial_indices = range(0, len(initial_schemes))

# Generate embeddings for all schemes
print("Generating embeddings for all schemes...")
embeddings = model.encode(all_schemes)
print("Embeddings generated successfully.\n")

# Compute cosine similarity matrix
print("Computing cosine similarity matrix...")
similarity_matrix = cosine_similarity(embeddings)
print("Cosine similarity matrix computed successfully.\n")

# Function to calculate novelty scores per module
def calculate_novelty_per_module(similarity_matrix, step_indices, scheme_to_module, initial_indices, modules):
    """
    Calculate novelty scores for each step, categorized by module.

    Parameters:
    - similarity_matrix: Cosine similarity matrix
    - step_indices: List of tuples indicating the start and end indices of schemes per step
    - scheme_to_module: List mapping each scheme to its module
    - initial_indices: Range of initial schemes
    - modules: Set of all module names

    Returns:
    - novelty_scores_avg: Average novelty scores per step
    - novelty_scores_max: Maximum novelty scores per step
    """
    novelty_scores_avg = []
    novelty_scores_max = []
    
    for i, (start, end) in enumerate(step_indices):
        method = methods[i]
        if method == 'Initial':
            novelty_scores_avg.append(0)
            novelty_scores_max.append(0)
            print(f"Step {i+1} ({method}): Initial step, novelty scores set to 0.")
            continue
        
        # Collect new schemes and their corresponding modules
        new_schemes_indices = range(start, end)
        module_to_new_indices = {}
        for idx in new_schemes_indices:
            module = scheme_to_module[idx]
            if module not in module_to_new_indices:
                module_to_new_indices[module] = []
            module_to_new_indices[module].append(idx)
        
        # Calculate novelty per module and then average
        module_novelty_avg = []
        module_novelty_max = []
        for module in modules:
            if module not in module_to_new_indices:
                continue  # No new schemes for this module in this step
            new_indices = module_to_new_indices[module]
            if not new_indices:
                continue
            
            # Find baseline indices for this module
            baseline_indices = [idx for idx in initial_indices if scheme_to_module[idx] == module]
            if not baseline_indices:
                avg_similarity = 0
                max_similarity = 0
            else:
                similarities = similarity_matrix[np.ix_(new_indices, baseline_indices)]
                avg_similarity = np.mean(similarities)
                max_similarity = np.max(similarities)
            
            # Calculate novelty scores
            module_novelty_avg.append(1 - avg_similarity)
            module_novelty_max.append(1 - max_similarity)
            print(f"Step {i+1} ({method}), Module '{module}': Avg Novelty = {1 - avg_similarity:.4f}, Max Novelty = {1 - max_similarity:.4f}")
        
        # Average across all modules
        if module_novelty_avg:
            overall_avg = np.mean(module_novelty_avg)
            novelty_scores_avg.append(overall_avg)
        else:
            novelty_scores_avg.append(0)
        
        if module_novelty_max:
            overall_max = np.mean(module_novelty_max)
            novelty_scores_max.append(overall_max)
        else:
            novelty_scores_max.append(0)
    
    return {'avg_cosine': novelty_scores_avg, 'max_cosine': novelty_scores_max}

print("Calculating novelty scores per module (baseline: Initial step)...")
novelty_scores = calculate_novelty_per_module(similarity_matrix, step_indices, scheme_to_module, initial_indices, module_set)
print(f"\nNovelty Scores per step: {novelty_scores}\n")

# Function to perform dimensionality reduction
def perform_dimensionality_reduction(embeddings, method='PCA'):
    """
    Perform dimensionality reduction.

    Parameters:
    - embeddings: High-dimensional embeddings
    - method: Dimensionality reduction method ('PCA', 't-SNE', 'UMAP')

    Returns:
    - embeddings_2d: 2D embeddings
    """
    if method == 'PCA':
        reducer = PCA(n_components=2)
    elif method == 't-SNE':
        reducer = TSNE(n_components=2, perplexity=30, n_iter=1000, random_state=42)
    elif method == 'UMAP':
        reducer = UMAP(n_components=2, random_state=42)
    else:
        raise ValueError("Unsupported dimensionality reduction method.")
    
    print(f"Performing {method} dimensionality reduction...")
    embeddings_2d = reducer.fit_transform(embeddings)
    print(f"{method} dimensionality reduction completed.\n")
    return embeddings_2d

# 执行PCA降维，并赋值给 embeddings_2d
print("Performing PCA for dimensionality reduction...")
embeddings_2d = perform_dimensionality_reduction(embeddings, method='PCA')

# Function to calculate design space coverage and diversity per module
def calculate_design_space_metrics_per_module(embeddings_2d, step_indices, scheme_to_module, modules):
    """
    Calculate design space coverage and internal diversity for each step, categorized by module.

    Parameters:
    - embeddings_2d: 2D embeddings of schemes
    - step_indices: List of tuples indicating the start and end indices of schemes per step
    - scheme_to_module: List mapping each scheme to its module
    - modules: Set of all module names

    Returns:
    - coverage_metrics_avg: Average coverage area per step
    - diversity_metrics_avg: Average internal diversity per step
    """
    coverage_metrics_avg = []
    diversity_metrics_avg = []
    
    for i, (start, end) in enumerate(step_indices):
        method = methods[i]
        step_embeddings = embeddings_2d[start:end]
        
        # Calculate coverage using Convex Hull
        if len(step_embeddings) < 3:
            area = 0
            print(f"Step {i+1} ({method}): Less than 3 schemes, coverage area set to 0.")
        else:
            hull = ConvexHull(step_embeddings)
            area = hull.area
            print(f"Step {i+1} ({method}): Coverage area = {area:.4f}")
        coverage_metrics_avg.append(area)
        
        # Calculate internal diversity using average pairwise cosine distance
        if len(step_embeddings) < 2:
            diversity = 0
            print(f"Step {i+1} ({method}): Less than 2 schemes, internal diversity set to 0.")
        else:
            distance_matrix = pairwise_distances(step_embeddings, metric='cosine')
            # Exclude self-distance by setting diagonal to NaN
            np.fill_diagonal(distance_matrix, np.nan)
            diversity = np.nanmean(distance_matrix)
            print(f"Step {i+1} ({method}): Internal diversity = {diversity:.4f}")
        diversity_metrics_avg.append(diversity)
    
    return coverage_metrics_avg, diversity_metrics_avg

print("Calculating design space coverage and internal diversity per step...")
coverage_metrics, diversity_metrics = calculate_design_space_metrics_per_module(
    embeddings_2d, step_indices, scheme_to_module, module_set
)
print(f"\nDesign Space Areas per step: {coverage_metrics}")
print(f"Internal Diversity per step: {diversity_metrics}\n")



# Function to plot design space coverage
def plot_design_space(embeddings_2d, step_indices, scheme_to_module, method_name):
    """
    Plot design space coverage.

    Parameters:
    - embeddings_2d: 2D embeddings of schemes
    - step_indices: List of tuples indicating the start and end indices of schemes per step
    - scheme_to_module: List mapping each scheme to its module
    - method_name: Name of the dimensionality reduction method for titles and filenames
    """
    plt.figure(figsize=(12, 8))
    colors = plt.cm.get_cmap('tab10', len(methods))
    color_map = {method: colors(i) for i, method in enumerate(methods)}
    
    for i, (start, end) in enumerate(step_indices):
        method = methods[i]
        color = color_map[method]
        step_schemes = embeddings_2d[start:end]
        plt.scatter(step_schemes[:, 0], step_schemes[:, 1], 
                    color=color, label=method, edgecolors='k', s=100, alpha=0.7)
        for j, (x, y) in enumerate(step_schemes):
            scheme = all_schemes[start + j]
            plt.text(x + 0.02, y + 0.02, scheme, fontsize=8)
    
    plt.title(f'Design Space Coverage with {method_name}')
    plt.xlabel(f'{method_name} Component 1')
    plt.ylabel(f'{method_name} Component 2')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    # Save the plot
    coverage_plot_path = os.path.join(output_dir, f'design_space_coverage_{method_name.lower()}.png')
    plt.savefig(coverage_plot_path)
    print(f"Design space coverage plot ({method_name}) saved to {coverage_plot_path}.\n")
    plt.close()

# Visualization of Novelty Scores
print("Plotting Novelty Scores...")
plt.figure(figsize=(10, 6))
steps = list(range(1, len(methods) + 1))
for metric in novelty_scores:
    plt.plot(steps, novelty_scores[metric], marker='o', linestyle='-', label=metric.replace('_', ' ').title())
    for i, txt in enumerate(novelty_scores[metric]):
        plt.annotate(f"{txt:.2f}", (steps[i], novelty_scores[metric][i]), textcoords="offset points", xytext=(0,10), ha='center')
plt.title('Novelty Scores per Design Method Step')
plt.xlabel('Design Method Steps')
plt.ylabel('Novelty Score (1 - Similarity)')
plt.xticks(steps, methods, rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()
# Save the plot
novelty_plot_path = os.path.join(output_dir, 'novelty_scores.png')
plt.savefig(novelty_plot_path)
print(f"Novelty scores plot saved to {novelty_plot_path}.\n")
plt.close()

# Visualization of Design Space Coverage Areas
print("Plotting Design Space Coverage Areas...")
plt.figure(figsize=(10, 6))
plt.bar(steps, coverage_metrics, color='skyblue', edgecolor='k')
for i, area in enumerate(coverage_metrics):
    plt.text(steps[i], area + 0.01, f"{area:.2f}", ha='center', va='bottom')
plt.title('Design Space Coverage Areas per Design Method Step')
plt.xlabel('Design Method Steps')
plt.ylabel('Design Space Coverage Area')
plt.xticks(steps, methods, rotation=45)
plt.grid(axis='y')
plt.tight_layout()
# Save the plot
area_plot_path = os.path.join(output_dir, 'design_space_areas.png')
plt.savefig(area_plot_path)
print(f"Design space coverage areas plot saved to {area_plot_path}.\n")
plt.close()

# Visualization of Internal Diversity
print("Plotting Internal Diversity...")
plt.figure(figsize=(10, 6))
plt.bar(steps, diversity_metrics, color='lightgreen', edgecolor='k')
for i, diversity in enumerate(diversity_metrics):
    plt.text(steps[i], diversity + 0.01, f"{diversity:.2f}", ha='center', va='bottom')
plt.title('Internal Diversity per Design Method Step')
plt.xlabel('Design Method Steps')
plt.ylabel('Internal Diversity (Average Cosine Distance)')
plt.xticks(steps, methods, rotation=45)
plt.grid(axis='y')
plt.tight_layout()
# Save the plot
diversity_plot_path = os.path.join(output_dir, 'internal_diversity.png')
plt.savefig(diversity_plot_path)
print(f"Internal diversity plot saved to {diversity_plot_path}.\n")
plt.close()

# Perform PCA, t-SNE, and UMAP and plot design space coverage
print("Plotting Design Space Coverage with PCA...")
plot_design_space(embeddings_2d, step_indices, scheme_to_module, 'PCA')

# Perform t-SNE
embeddings_tsne = perform_dimensionality_reduction(embeddings, method='t-SNE')
print("Plotting Design Space Coverage with t-SNE...")
plot_design_space(embeddings_tsne, step_indices, scheme_to_module, 't-SNE')

# Perform UMAP
try:
    embeddings_umap = perform_dimensionality_reduction(embeddings, method='UMAP')
    print("Plotting Design Space Coverage with UMAP...")
    plot_design_space(embeddings_umap, step_indices, scheme_to_module, 'UMAP')
except AttributeError as e:
    print(f"Error: {e}")
    print("Ensure that the 'umap-learn' library is installed correctly. You can install it using 'pip install umap-learn'.")

# 对 t-SNE 和 UMAP 生成的二维嵌入计算凸包面积
print("Calculating design space coverage for t-SNE...")
coverage_metrics_tsne, diversity_metrics_tsne = calculate_design_space_metrics_per_module(
    embeddings_tsne, step_indices, scheme_to_module, module_set
)
print(f"t-SNE Design Space Areas per step: {coverage_metrics_tsne}")
print(f"t-SNE Internal Diversity per step: {diversity_metrics_tsne}\n")

print("Calculating design space coverage for UMAP...")
coverage_metrics_umap, diversity_metrics_umap = calculate_design_space_metrics_per_module(
    embeddings_umap, step_indices, scheme_to_module, module_set
)
print(f"UMAP Design Space Areas per step: {coverage_metrics_umap}")
print(f"UMAP Internal Diversity per step: {diversity_metrics_umap}\n")

print("All steps completed. Please check the 'output_plots' directory for the saved images.")
