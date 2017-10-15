''' BFS: Shortest Reach in a Graph '''

class Graph(object):
    ''' Graph '''

    def __init__(self, nodes):
        pass

    def connect(self, node_1, node_2):
        ''' creates an edge from node_1 to node_2 '''
        pass

    def find_all_distances(self, node_index):
        '''
        calculates distance between the given node and all other nodes
        in the graph
        '''
        pass


def main():
    ''' Main function '''

    num_queries = int(input())
    for _ in range(num_queries):
        nodes, edges = [int(value) for value in input().split()]
        graph = Graph(nodes)

        for _ in range(edges):
            node_1, node_2 = [int(x) for x in input().split()]
            graph.connect(node_1 - 1, node_2 - 1)

        starting_node_index = int(input())
        graph.find_all_distances(starting_node_index - 1)

if __name__ == '__main__':
    main()
