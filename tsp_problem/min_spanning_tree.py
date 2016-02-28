from collections import defaultdict
from heapq import *

class mini_tree_length:

    #calculate the minimum spanning tree

    def prim(self, nodes, edges ):
        conn = defaultdict( list )
        for n1,n2,c in edges:

            conn[ n1 ].append( (c, n1, n2) )
            conn[ n2 ].append( (c, n2, n1) )

        mst = []
        used = set( nodes[ 0 ] )
        usable_edges = conn[ nodes[0] ][:]
        heapify( usable_edges )

        while usable_edges:
            cost, n1, n2 = heappop( usable_edges )
            if n2 not in used:
                used.add( n2 )

                # if self.check_node_twice(n1, n2, mst):
                mst.append( ( n1, n2, cost ) )

                for e in conn[ n2 ]:
                    if e[ 2 ] not in used:
                        heappush( usable_edges, e )

        # print list(conn.items())
        return mst


    def calculate_unvisited_node(self, unvisited_nodes):
        number_of_unvisited = len(unvisited_nodes)
        edges = []
        nodes_str = ""

        for i in range(0, number_of_unvisited, 1):
            nodes_str = nodes_str + unvisited_nodes[i].name

            for j in range(i+1, number_of_unvisited, 1):

                c1 = unvisited_nodes[i]
                c2 = unvisited_nodes[j]
                edges.append((c1.name, c2.name,c1.next_distance(c2)))

        nodes = list(nodes_str)
        prim_tree = self.prim(nodes, edges)
        # print prim_tree

        mst_length = 0
        for p in prim_tree:
            mst_length = mst_length + p[2]

        return mst_length










#test
# nodes = list("ABCDEFG")
# edges = [ ("A", "B", 7), ("A", "D", 5),
#           ("B", "C", 8), ("B", "D", 9), ("B", "E", 7),
#       ("C", "E", 5),
#       ("D", "E", 15), ("D", "F", 6),
#       ("E", "F", 8), ("E", "G", 9),
#       ("F", "G", 11)]
#
# print "prim:", prim( nodes, edges )
#output
#prim: [('A', 'D', 5), ('D', 'F', 6), ('A', 'B', 7), ('B', 'E', 7), ('E', 'C', 5), ('E', 'G', 9)]
