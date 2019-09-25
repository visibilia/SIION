
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


from sklearn.cluster import DBSCAN
from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering
from utils.utils import distance_in_kilometers
NOT_IN_A_CLUSTER = -1

"""
File containing clustering algorithms. 
Some functions are interfaces to the sci-kit learn algorithms and some are full implementations. 
"""


def highest_attribute_value(df, attribute_name='checkins', threshold=5):
    """Clustering algorithm based on main attribute.

    Parameters
    ----------

    df : A pandas dataframe containing the latitude and longitude data that will be clusterized. The columns of
    the dataframe must have the names 'latitude' and 'longitude'

    attribute_name : str
        column name of the attribute that will be used to select the center venues of each cluster.

    threshold : float
        the euclidian distance threshold.

    Returns
    -------
    df : a pandas dataframe with the column 'cluster_id' that identifies the cluster of each row of the dataframe.
    """
    # Sorting the values of the dataframe by attribute in the descending order.
    df = df.sort_values(attribute_name, ascending=False)
    # Creating a new column 'cluster_id' that represents the cluster index of that venue,
    # not considering overlapping.
    current_cluster_index = 0
    clusters_indexes = [NOT_IN_A_CLUSTER] * len(df)
    for venue in df.itertuples():
        if clusters_indexes[venue.Index] == NOT_IN_A_CLUSTER:
            # Assigns the cluster id value to the venue.
            clusters_indexes[venue.Index] = current_cluster_index
            for neighbor in df.itertuples():
                if (venue.Index != neighbor.Index) and (distance_in_kilometers(
                        venue.latitude, venue.longitude, neighbor.latitude, neighbor.longitude)
                            <= float(threshold)) and (clusters_indexes[neighbor.Index] == NOT_IN_A_CLUSTER):
                        clusters_indexes[neighbor.Index] = current_cluster_index
            # Iterates the cluster index to the next cluster id.
            current_cluster_index += 1
    df.sort_index(inplace=True)
    df['cluster_id'] = clusters_indexes
    return df


def kmeans(df, n_clusters=100):
    """Interface to kmeans sci-kit learn algorithm

    Parameters
    ----------

    df : A pandas dataframe containing the latitude and longitude data that will be clusterized. The columns of
    the dataframe must have the names 'latitude' and 'longitude'

    n_clusters : int
        number of clusters to the k-means algorithm.
    Returns
    -------
    df : a pandas dataframe with the column 'cluster_id' that identifies the cluster of each row of the dataframe.
    """
    mat = df[['latitude', 'longitude']].values
    km = KMeans(n_clusters=int(n_clusters)).fit(mat)
    df['cluster_id'] = km.labels_
    return df


def dbscan(df, eps=0.001, min_samples=3):
    """Interface to dbscan sci-kit learn algorithm

    Parameters
    ----------

    df : A pandas dataframe containing the latitude and longitude data that will be clusterized. The columns of
    the dataframe must have the names 'latitude' and 'longitude'

    eps : float
        eps parameter to the dbscan sci-kit learn algorithm.

    min_samples: int
        min_samples parameter to the dbscan sci-kit learn algorithm.

    Returns
    -------
    df : a pandas dataframe with the column 'cluster_id' that identifies the cluster of each row of the dataframe.
    """
    mat = df[['latitude', 'longitude']].values
    db = DBSCAN(eps=float(eps), min_samples=int(min_samples), metric='euclidean').fit(mat)
    df['cluster_id'] = db.labels_
    return df


def agglomerative_clustering(df, n_clusters=100):
    """Interface to agglomerative clustering (bottom-up hierarchical clustering) sci-kit learn algorithm

    Parameters
    ----------

    df : A pandas dataframe containing the latitude and longitude data that will be clusterized. The columns of
    the dataframe must have the names 'latitude' and 'longitude'

    n_clusters : int
        number of clusters to the agglomerative clustering algorithm.

    Returns
    -------
    df : a pandas dataframe with the column 'cluster_id' that identifies the cluster of each row of the dataframe.
    """
    mat = df[['latitude', 'longitude']].values
    ag = AgglomerativeClustering(n_clusters=int(n_clusters)).fit(mat)
    df['cluster_id'] = ag.labels_
    return df

