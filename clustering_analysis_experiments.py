
#########################################################
##         VISIBILIA
## Project: SIION
## Year:    2018-2019 
## Members: 
##          Vinicius Ferreira @viniciusferreiradasilva         
## 		    Alan Valejo @alanvalejo
##          Paola Valdivia @paolavaldivia
##          Jorge Valverde-Rebaza @jvalverr
##
## Site:    http://visibilia.net.br/siion-resources-bracis-2019/
##
#########################################################

from __future__ import print_function
from sklearn.metrics import silhouette_samples, silhouette_score
from collections import Counter
from preprocessing.file_loading import json_2_dataframe
from preprocessing.file_loading import load_attribute
from algorithms.clustering import highest_attribute_value
from algorithms.clustering import kmeans
from algorithms.clustering import dbscan
from algorithms.clustering import agglomerative_clustering
from utils.utils import str2bool

import numpy as np
import argparse


# Instantiate the parser
parser = argparse.ArgumentParser(description='Map segmentation tool.', formatter_class=argparse.RawTextHelpFormatter)

# Required input_file name argument.
parser.add_argument('--input_file', required=True, type=str,
                    help='A string representing a .json input file path with latitude and longitude columns.')

# Optional output_file dir argument.
parser.add_argument('--output_dir', type=str, help="A string representing an output dir path to save the clustering"
                                                   " map, the resulting network .ncol file and the resulting embeddings"
                    , required=True)

# Required input_file name argument.
parser.add_argument('--map', required=True, type=str, default='false',
                    help='A string representing a .json input file path with latitude and longitude columns.')


# Required clustering algorithm argument.
parser.add_argument('--clustering_algorithm', type=int, required=True,
                    help='An integer representing the clustering algorithm that will be used to segment the map:\n'
                         '1 - Highest attribute. Args: attribute_name (str), threshold (float),\n'
                         '2 - K-means. Args: n_clusters (int),\n'
                         '3 - DBSCAN. Args eps (float), min_samples (int),\n'
                         '4 - Agglomerative clustering. Args: n_clusters (int)\n')

# Required clustering algorithm configs.
parser.add_argument('--configs', required=False, nargs='+', default=[],
                    help='List of configs that will be passed to the clustering algorithm. Each clustering algorithm '
                         'has a certain number of parameters. You should pass them in the same order as strings:\n'
                         '--configs "CONF_1", "CONF_2",... "CONF_N".')


args = parser.parse_args()
# Retrieve the configs from arguments.
configs = [list(map(lambda x: float(x) if x.isdigit() else x, x)) for x in list(map((lambda x: x.strip().split(' ')),
                                                                                    args.configs))]

# Loading a json file for a pandas dataframe.
print("loading data " + args.input_file)
df = json_2_dataframe(args.input_file)
# Loading check-in list to the dataframe.
df = load_attribute(df, 'data/input/filtered/checkins.json', 'business_id', 'checkins')
# List containing all the implemented clustering algorithms.
clustering_algorithms = [highest_attribute_value, kmeans, dbscan, agglomerative_clustering]
# Retrieve the matrix formed by latitude and longitude.
X = df[['latitude', 'longitude']].values
# It will be map plotting?
plot_map = str2bool(args.map)
# Var that save all silhouettes.
silhouettes = np.empty(len(configs))
ns_clusters = np.empty(len(configs))
for index, config in enumerate(configs):
    print('config:', config)
    # Clustering
    cluster_labels = np.array(clustering_algorithms[args.clustering_algorithm](df, *config)['cluster_id'])
    ns_clusters[index] = len(Counter(cluster_labels).keys())

    # The silhouette_score gives the average value for all the samples.
    # This gives a perspective into the density and separation of the formed
    # clusters
    silhouette_avg = silhouette_score(X, cluster_labels)
    # Tests if the current config is better than the current best.
    silhouettes[index] = silhouette_avg
    # Compute the silhouette scores for each sample
    sample_silhouette_values = silhouette_samples(X, cluster_labels)

clustering_file = args.output_dir + args.input_file.split('/')[-1].split('.')[0] + '_' + clustering_algorithms[
        args.clustering_algorithm].__name__ + '.csv'
print("saving clustering analysis into:", clustering_file)
# Writing the embedding into a file.
with open(clustering_file, 'w') as f:
    for index, silhouette in enumerate(silhouettes):
        f.write(','.join(map(str, configs[index])) + ',' + str(silhouette) + ',' + str(ns_clusters[index]) + '\n')
f.close()
