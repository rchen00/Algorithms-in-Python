"""
Project (Week 7)

You may select only one of following two projects:

P1:
Experiment with the efficiency of the find() method of Python’s str class and develop a hypothesis about which pattern-matching algorithm it uses. Try using inputs that are likely to cause both best-case and worst-case running times for various algorithms. Describe your experiments and your conclusions.

P2:
There are eight small islands in a lake, and the state wants to build bridges to connect them so that each island can be reached from any other islands via one or more bridges. Assume the cost of constructing a bridge is proportional to its length. The distances between pairs of islands are in the following table.
	 		2	3	4	5	6	7	8
 		1	240	210	340	280	200	345	120
		2		265	175	215	180	185	155
		3			260	115	350	435	195
		4				160	330	295	230
		5					360	400	170
		6						175	205
		7							305	
a.	Find which bridges to build to minimize the total construction cost.
b.	What if the state wants each island should be reached from any other islands via no more than two bridges? Is there a known algorithm to solve this problem? What would you do?  			

Submit your code together with the run results and your conclusions/solutions.

"""

# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 21:14:10 2021

@author: robert
"""
from partition import Partition
from priority_queue_base import PriorityQueueBase
from heap_priority_queue import HeapPriorityQueue
from graph import Graph
from mst import MST_Kruskal
from shortest_paths import shortest_path_lengths
from shortest_paths import shortest_path_tree


def graph_from_edgelist(E, directed=False):
  """Make a graph instance based on a sequence of edge tuples.

  Edges can be either of from (origin,destination) or
  (origin,destination,element). Vertex set is presume to be those
  incident to at least one edge.

  vertex labels are assumed to be hashable.
  """
  g = Graph(directed)
  V = set()
  for e in E:
    V.add(e[0])
    V.add(e[1])

  verts = {}  # map from vertex label to Vertex instance
  for v in V:
    verts[v] = g.insert_vertex(v)

  for e in E:
    src = e[0]
    dest = e[1]
    element = e[2] if len(e) > 2 else None
    g.insert_edge(verts[src],verts[dest],element)

  return g

def R_14_27():
    """Return the weighted, undirected graph from R-14-27
    """
    E=(
   ('1','2',240),('1','3',210),('1','4',340),('1','5',280),('1','6',200),('1','7',345),('1','8',120),
   ('2','3',265),('2','4',175),('2','5',215),('2','6',180),('2','7',185),('2','8',155),
   ('3','4',260),('3','5',115),('3','6',350),('3','7',435),('3','8',195),
   ('4','5',160),('4','6',330),('4','7',295),('4','8',230),
   ('5','6',360),('5','7',400),('5','8',170),
   ('6','7',175),('6','8',205),
   ('7','8',305),
   )
    return graph_from_edgelist(E, False)


g=R_14_27()
print(g)
d=MST_Kruskal(g)
print("minimum cost bridges:",d)
print("from", "\tto", "\tdistance")
total=0
for e in d:
    total += e.element()
    print(e.endpoints()[0].element(), "\t\t",e.endpoints()[1].element(),"\t\t" , e.element())
print("the minimum total length of the bridges is: ",total)    

""" make each island to another island one hop """

def hop_R_14_27():
    
    E=(
   ('1','2',1),('1','3',1),('1','4',1),('1','5',1),('1','6',1),('1','7',1),('1','8',1),
   ('2','3',1),('2','4',1),('2','5',1),('2','6',1),('2','7',1),('2','8',1),
   ('3','4',1),('3','5',1),('3','6',1),('3','7',1),('3','8',1),
   ('4','5',1),('4','6',1),('4','7',1),('4','8',1),
   ('5','6',1),('5','7',1),('5','8',1),
   ('6','7',1),('6','8',1),
   ('7','8',1),
   )    

    return graph_from_edgelist(E, False)

g=hop_R_14_27()
print("\nGraph of hops:", g)
for u in g.vertices():
    if u.element() == "1":
        s = u
        break

cloud,d = shortest_path_lengths(g, s)
print("\nCloud Map:\n",cloud)

for v in cloud.keys():
    print(v.element(),cloud[v])

print("\nDistance Map:\n",d)
for v in d.keys():
    print(v.element(),d[v])

t=shortest_path_tree(g,s,d)
print("\nShortest Path Tree: \n",t)
for v in t.keys():
    print(t[v])
    
"""
The shortest path algorism will find that, take any island as root, from the root island to any other island, 
the maximum hops is one. Then any non root island to reach any other island, the maximum hops will be 2  

"""
