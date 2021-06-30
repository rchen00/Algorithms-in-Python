# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 10:56:22 2021

@author: robert
"""

from mst import MST_Kruskal
from graph_examples import graph_from_edgelist


def final_q9():
  """Return the unweighted, directed graph from Figure 14.3 of DSAP."""
  E = (
    ('s','a',1), ('s','t',4), ('s','b',1),
    ('a','c',1), ('c','t',1), ('b','d',2), ('d','t',2),
    )
  return graph_from_edgelist(E, False)

g=final_q9()
d=MST_Kruskal(g)

print("minimum cost bridges:",d)
print("from", "\tto", "\tdistance")
total=0
for e in d:
    total += e.element()
    print(e.endpoints()[0].element(), "\t\t",e.endpoints()[1].element(),"\t\t" , e.element())
print("the minimum total length of the bridges is: ",total) 