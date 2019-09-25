
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



from math import sin, cos, sqrt, atan2, radians
import argparse


# Calculates the distance between node and neighbor in km using latitude and longitude.
def distance_in_kilometers(latitude_from, longitude_from, latitude_to, longitude_to):
    # Approximate earth radius.
    R = 6373.0
    latitude_from = radians(latitude_from)
    longitude_from = radians(longitude_from)
    latitude_to = radians(latitude_to)
    longitude_to = radians(longitude_to)
    dlon = longitude_to - longitude_from
    dlat = latitude_to - latitude_from
    a = sin(dlat / 2) ** 2 + cos(latitude_from) * cos(latitude_to) * sin(dlon / 2) ** 2
    return R * (2 * atan2(sqrt(a), sqrt(1 - a)))


# Converts a str input to boolean.
def str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'verdadeiro', 'v', 'y', '1', 'sim', 's'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'falso', 'f', 'n', '0', 'nao', 'não', 'n'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')
