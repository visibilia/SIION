
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

import igraph

"""
File containing functions to build networks. Those functions are interfaces to the python igraph library.
"""


def create_network(n_vertices, id_attribute=None, attributes=None):
    """Creates a network adding vertices and vertices attributes.

    Parameters
    ----------

    n_vertices: int
    Number of vertices that will be added to the network.

    id_attribute: str
    Name of the node attribute that will be added to the network.

    attributes:
    List of attributes that will be added to the vertex list. The size of the list must be equal to the n_vertices.

    Returns
    -------
    g: a python igraph network object.
    """
    g = igraph.Graph()
    g.add_vertices(n_vertices)
    # Assigns the vertices id attributes to the vertices of the network.
    if attributes:
        g.vs[id_attribute] = attributes
    return g


def add_edges(g, edge_list):
    """Add edges to the network g.

    Parameters
    ----------

    g : a python igraph network object.

    edge_list: a list of edges for adding to the network. A edge between v and u has the format of a tuple (u, v).

    Returns
    -------
    g: a network with the edges of edge_list.
    """
    g.add_edges(edge_list)
    return g


def add_weighted_edges(g, edge_list, edges_weights):
    """Add weighted edges to the network g.

    Parameters
    ----------

    g : a python igraph network object.

    edge_list: a list of edges for adding to the network. A edge between v and u has the format of a tuple (u, v).

    edges_weights: a list of double values representing the edges weights. A edge between v and u has the
    format of a tuple (u, v).

    Returns
    -------
    g: a network with the edges of edge_list.
    """
    g.add_edges(edge_list)
    g.es['weight'] = edges_weights
    return g
