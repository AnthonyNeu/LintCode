"""
Find the number Weak Connected Component in the directed graph. 
Each node in the graph contains a label and a list of its neighbors. (a connected set of a directed graph is a subgraph in which any two vertices are connected by direct edge path.)

Example
Given graph:

A----->B  C
 \     |  | 
  \    |  |
   \   |  |
    \  v  v
     ->D  E <- F
Return {A,B,D}, {C,E,F}. Since there are two connected component which are {A,B,D} and {C,E,F}
"""

# Definition for a directed graph node
# class DirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []
class union_find:
    def __init__(self, node_set):
        self.father = {}
        for label in node_set:
            self.father[label] = label
    
    def find(self, x):
        parent = self.father[x]
        while parent != self.father[parent]:
            parent = self.father[parent]
        return parent
    
    def compressed_find(self, x):
        parent = self.father[x]
        while parent != self.father[parent]:
            parent = self.father[parent]
        # set all father to be parent we just get
        prev_father = self.father[x]
        while prev_father != self.father[prev_father]:
            prev_father, self.father[prev_father] = self.father[prev_father], parent
        return parent
    
    def union(self, x, y):
        father_x = self.find(x)
        father_y = self.find(y)
        if father_x != father_y:
            self.father[father_x] = father_y

class Solution:
    # @param {DirectedGraphNode[]} nodes a array of directed graph node
    # @return {int[][]} a connected set of a directed graph
    def connectedSet2(self, nodes):
        # Write your code here
        from sets import Set
        node_set = Set()
        for node in nodes:
            node_set.add(node.label)
            for neighbor in node.neighbors:
                node_set.add(neighbor.label)
        uf = union_find(node_set)
        for node in nodes:
            node_father = uf.find(node.label)
            for neighbor in node.neighbors:
                neighbor_father = uf.find(neighbor.label)
                if node_father != neighbor_father:
                    uf.union(node.label, neighbor.label)
        
        def find_wcc():
            from collections import defaultdict
            wcc_dict = {}
            for label in node_set:
                node_father = uf.find(label)
                if node_father not in wcc_dict:
                    wcc_dict[node_father] = [label]
                else:
                    wcc_dict[node_father].append(label)
            for key, value in wcc_dict.iteritems():
                value.sort()
                wcc.append(value)
        wcc = []
        find_wcc()
        return wcc
