
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


import numpy as np

"""
File containing embedding strategies to embed districts categories to recomendation.
"""


def embedding_by_category_probability(categories, districts_categories_count):
    """Clustering algorithm based on main attribute.

    Parameters
    ----------

    categories : A python dict containing all the categories in the dataframe.

    districts_categories_count : A python list where each object is a dict representing a district. The keys of the dict
    represent the the categories ids and the values represent the counting of appearances of that category.

    Returns
    -------
    districts_categories_embedding: a numpy matrix representing the embeddings where each line is a district.
    """
    districts_categories_embedding = np.empty((len(districts_categories_count), len(categories)))

    for district_id, district in enumerate(districts_categories_count):
        # Calculates the value of embedding for every present category.
        embedding_values = np.divide(list(district.values()), np.sum(list(district.values())))
        # Merges an empty district embedding to the existent district embedding to give zero value to non-present
        # categories.
        district_embedding = np.asarray(list({**dict(zip(categories, np.zeros(len(categories)))),
                                              **dict(zip(district.keys(), embedding_values))}.values()))
        # Add the district embedding to the embedding dictionary.
        districts_categories_embedding[district_id] = district_embedding

    return districts_categories_embedding
