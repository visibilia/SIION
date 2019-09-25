
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


from sklearn.metrics.pairwise import euclidean_distances

import numpy as np


# A recommendation algorithm that uses the knn algorithm to recommend.
def nearest_district(df_training, df_test, categories, training_embedding, test_embedding):
    """
    For each test instance, calculates the nearest district using only the test categories.

    Parameters
    ----------

    df_training : A dataframe used to get the training embeddings.

    df_test: A dataframe containing the test patterns.

    categories: All the categories of the dataset.

    training_embedding: the district embeddings of the venues.

    test_embedding: the test embedding generated using the df_test patterns.

    Returns
    -------
    predicted_districts: a list containing the predicted scores of the test set.
    """
    # Creates an empty matrix distance.
    labels = [None] * len(test_embedding)
    for index, test in enumerate(test_embedding):
        # Recover the non-zero indexes.
        non_zero_indexes = np.nonzero(test)[0]
        labels[index] = np.argmin(euclidean_distances(test[non_zero_indexes].reshape(1, -1),
                                                      training_embedding[:, non_zero_indexes]))
    return labels


# A recommendation algorithm that uses the knn algorithm to recommend.
def nearest_district_for_all_categories(df_training, df_test, categories, district_embedding, test_embedding):
    """
    For each test instance, calculates the nearest district using all the categories.

    Parameters
    ----------

    df_training : A dataframe used to get the training embeddings.

    df_test: A dataframe containing the test patterns.

    categories: All the categories of the dataset.

    training_embedding: the district embeddings of the venues.

    test_embedding: the test embedding generated using the df_test patterns.

    Returns
    -------
    predicted_districts: a list containing the predicted scores of the test set.
    """
    distance_matrix = euclidean_distances(district_embedding, test_embedding).transpose()
    # print("categories:\n", categories)
    # print('-' * 50)
    # print("district_embedding:\n", district_embedding.shape)
    # print('-' * 50)
    # print("test_embedding:\n", test_embedding.shape)
    # print('-' * 50)
    # print("distance_matrix:\n", distance_matrix.shape)
    return [np.argmin(distance_matrix[x]) for x in range(len(distance_matrix))]




