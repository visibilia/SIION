
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



#!/usr/bin/python
from collections import Counter

import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

"""
File containing functions to plotting cluster maps according to the color of each cluster.
"""


def draw_cluster_map(df):
    """Draws a cluster map.

    Parameters
    ----------

    df : A pandas dataframe containing the latitude, longitude and cluster id data that will be clusterized.
    The columns of the dataframe must have the names 'latitude', 'longitude' and 'cluster_id'.

    Returns
    -------
    fig: a figure object of the matplotlib module.
    """
    fig = plt.figure()
    plt.scatter(df.latitude, df.longitude, marker='.', c=df.cluster_id)
    return fig


def draw_pointed_cluster_map(df, attribute='checkins'):
    """Draws a cluster map highlighting important points. The important point are calculated according to the attribute
    value.

    Parameters
    ----------

    df : A pandas dataframe containing the latitude, longitude and cluster id data that will be clusterized.
    The columns of the dataframe must have the names 'latitude', 'longitude' and 'cluster_id'.

    attribute: str
    The attribute column name in the pandas dataframe that will be used to highlight points on the map. Rows with higher
    values of attribute are more highlighted.

    Returns
    -------
    fig: a figure object of the matplotlib module.
    """
    fig = plt.figure()
    s = list(df[attribute]/(np.mean(df[attribute])))
    # 2nd Plot showing the actual clusters formed
    X = df[['latitude', 'longitude']].values
    cluster_labels = np.array(df['cluster_id']).astype(float)
    n_clusters = len(Counter(cluster_labels).keys())
    colors = cm.nipy_spectral(cluster_labels / n_clusters)
    # plt.scatter(df.latitude, df.longitude, marker='.', s=s, c=df.cluster_id)
    plt.scatter(X[:, 0], X[:, 1], marker='.', s=30, lw=0, alpha=0.7,
                c=colors, edgecolor='k')
    plt.xlabel('Latitude')
    plt.ylabel('Longitude')
    return fig


def save_map(fig, file_name):
    """Saves the map as a image file.

    Parameters
    ----------

    fig : figure object to matplotlib module;

    file_name : str.
    representing file path where the map will me saved.

    Returns
    -------
    None.
    """
    fig.savefig(file_name, format='eps')
    plt.close(fig)


def plot_map(fig):
    """Plots the map on the screen.

    Parameters
    ----------
   fig : figure object to matplotlib module;

    Returns
    -------
    None
    """
    plt.show(fig)


