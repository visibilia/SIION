# Recommender System for discovering of Business Opportunities (Still under construction)

This is the repo containing the code and other resources implemented for the article intitled "__Exploiting Geographical Data to improve Recommender Systems for Business Opportunities in Urban Areas__", which is published in the proceedings of [BRACIS 2019](http://www.bracis2019.ufba.br/). This framework is part of SIION project, so for ease of communication let's call the content of this repository also as __SIION__.

- Other resources related to the article: http://visibilia.net.br/siion-resources-bracis-2019/
- Details about SIION project: http://visibilia.net.br/siion/

## Features

SIION is a framework based on clustering and recommender systems to perform some tasks related to Geomarketing. Therefore, the main features are:

- __Geographic Map Partitioning.__ Given a geographic map corresponding to a specific target city, SIION apply a clustering algorithm to automatically partitioning the target city into a set of non-empty and non-overlapping geographical areas called business districts. To obtain appropriate business districts, the clustering algorithm used should consider different similarity relations among the business locations existing in the target city, e.g. geographical distance, economic factors, etc. In this version, SIION considers the following state-of-the-art clustering algorithms: Kmeans, DBSCAN, agglomerative hierarchical clustering (AC) and business district discovering (BDD). 

## Dependencies

In most cases you will want to follow the requirements defined in the requirements/*.txt files in the package. 

### Base dependencies
```
scipy
numpy
future
scikit-learn
pandas
matplotlib # for plot some clustering results
python-igraph # for generation of bipartitie graphs which are used in recommendation engines 
```



## Contributing

This project is open for contributions. Here are some of the ways for
you to contribute:

- Bug reports/fix
- Features requests
- Use-case demonstrations

In case you want to implement your own version of this framework, please 
read more details about [our article](http://visibilia.net.br/siion-resources-bracis-2019/) and [SIION project](http://visibilia.net.br/siion/) to help
you integrate your implementation in our framework.

To make a contribution, just fork this repository, push the changes
in your fork, open up an issue, and make a Pull Request!

We are also open to talk more about this project! Just go to our [contact form](http://visibilia.net.br/avaliacao-prototipo-siion/).


# Cite
If you used the material available in this repository in your research or project, please
cite [our work](https://www.researchgate.net/publication/336042054_Exploiting_Geographical_Data_to_improve_Recommender_Systems_for_Business_Opportunities_in_Urban_Areas):

```bibtex
@inproceedings{visibilia:siion:2019, 
 author = {Ferreira, Vin\'icius and Valejo, Alan and Valdivia, Paola and Valverde-Rebaza, Jorge},
 title = {Exploiting Geographical Data to improve Recommender Systems for Business Opportunities in Urban Areas},
 booktitle = {Proceedings of The 8th Brazilian Conference on Intelligent Systems},
 series = {BRACIS 2019},
 note = {To be published},
 location = {Salvador-Bahia, Brazil},
 year = {2019}
 }
```
