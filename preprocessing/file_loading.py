
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


import json
import pandas as pd

"""
A file containing functions to load information from json files.
"""


def filter_json_by_attribute(filename, attribute, value, output_path):
    """Filter a raw json file matching rows according to an attribute.

    Parameters
    ----------

    filename : an str representing the raw json file path.

    attribute: str representing an attribute json name that will be used to matching json rows.

    value: value of the attribute in the json raw file that will be used to filter the matched rows.

    output_path: an str representing the path of the output file.

    Returns
    -------
    None
    """
    output_file = open(output_path, 'w')  # open the output file.
    with open(filename) as fp:
        for line in fp:
            obj = json.loads(line)
            obj_value = str(obj[attribute])
            if obj_value == value:
                output_file.write(json.dumps(obj) + '\n')
    output_file.close()


def json_2_dataframe(filename):
    """Converts a json file to a pandas dataframe.

    Parameters
    ----------

    filename : a str representing the raw json file path.

    Returns
    -------
    pandas dataframe.
    """
    return pd.read_json(path_or_buf=filename, lines='true')


def load_attribute(df, filename, id_attribute, attribute, default_value=0):
    """Loads a column value present in a json file to a pandas dataframe as a column.

    Parameters
    ----------

    df: pandas dataframe that will receive a new column.

    filename : a str representing the raw json file path..

    id_attribute: str representing the name of the id attribute of the pandas dataframe rows to match to the rows of the
    raw json file.

    attribute: str representing the json attribute name that will compose the new column in the dataframe.

    default_value: default value of the attribute.
    Returns
    -------
    df: pandas dataframe with the new column.
    """
    # Loads the file that contains the attribute.
    df_attribute = pd.read_json(path_or_buf=filename)
    # Iterates over the ids present in both dataframe. This code also set the null cells to a default value.
    return df.reset_index().merge(df_attribute[[id_attribute, attribute]], left_index=True, left_on=id_attribute,
                    right_on=id_attribute, how='left').fillna({attribute: default_value}).set_index('index')

