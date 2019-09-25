
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
from sklearn.metrics import silhouette_score
from sklearn.metrics import silhouette_samples
from sklearn.metrics import average_precision_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import roc_auc_score

"""
File containing metrics to analyse clustering algorithms outputs and classifiers.
"""


def silhouette_coefficient(df):
    """Calculates the clustering silhouette coefficient for the clusterized data.

    Parameters
    ----------

    df : A pandas dataframe containing the latitude, longitude and cluster id data that will be clusterized.
    The columns of the dataframe must have the names 'latitude', 'longitude' and 'cluster_id'.

    Returns
    -------
    float representing the value of silhouette coefficient for that clustering.
    """
    return silhouette_score(df[['latitude', 'longitude']].values, df['cluster_id'])


def silhouette_sample(df):
    """Calculates the clustering silhouette coefficient for each sample of the clusterized data.

    Parameters
    ----------

    df : A pandas dataframe containing the latitude, longitude and cluster id data that will be clusterized.
    The columns of the dataframe must have the names 'latitude', 'longitude' and 'cluster_id'.

    Returns
    -------
    list of float representing the value of silhouette coefficient for sample in it's cluster.
    """
    return silhouette_samples(df[['latitude', 'longitude']].values, df['cluster_id'])


def pertinence(y_test, y_score):
    """Calculates the degree of pertinence of a venue in a district.

    Parameters
    ----------

    y_test : the real class of the pattern.

    y_score : the predicted class of the pattern.

    Returns
    -------
    the area under roc curve for the classified data.
    """
    pass
