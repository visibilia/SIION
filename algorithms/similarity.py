
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

import sklearn

"""
File containing similarity algorithms. The functions are interfaces to the sci-kit learn algorithms. 
"""


def cosine_similarity(x, y):
    """Cosine similarity.

    Parameters
    ----------

    x: A numpy matrix.

    y: A numpy matrix with the same number of columns as x.

    Returns
    -------
    cosine: the cosine similarity between x and y.
    """
    return sklearn.metrics.pairwise.cosine_similarity(x, y)


def euclidean_distances(x, y):
    """Euclidian distance.

    Parameters
    ----------

    x: A numpy matrix.

    y: A numpy matrix with the same number of columns as x.

    Returns
    -------
    euclidian: the euclidian distance between x and y.
    """
    return sklearn.metrics.pairwise.euclidean_distances(x, y)


def manhattan_distances(x, y):
    """Cosine similarity.

    Parameters
    ----------

    x: A numpy matrix.

    y: A numpy matrix with the same number of columns as x.

    Returns
    -------
    manhattan: the manhattan distances between x and y.
    """
    return sklearn.metrics.pairwise.manhattan_distances(x, y)
