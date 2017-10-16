''' BFS: Shortest Reach in a Graph '''

import queue


DISTANCE_FACTOR = 6

class Graph(object):
    ''' Graph '''

    def __init__(self, node_count):
        self.node_count = node_count
        self.edges = dict()
        self.distances = dict()
        for index in range(self.node_count):
            self.distances[index] = -1
            self.edges[index] = set()

    def connect(self, node_1, node_2):
        ''' creates an edge from node_1 to node_2 '''
        node_set = self.edges[node_1]
        node_set.add(node_2)
        self.edges[node_1] = node_set

    def find_all_distances(self, node_index):
        '''
        calculates distance between the given node and all other nodes
        in the graph
        '''
        possible_paths = queue.Queue()
        possible_paths.put(node_index)
        iteration = 1
        while not possible_paths.empty():
            current_node = possible_paths.get()
            for child_node in list(self.edges[current_node]):
                self.distances[child_node] = int(iteration * DISTANCE_FACTOR)
                possible_paths.put(child_node)
            iteration += 1

        sorted_distances = list()
        for index in range(self.node_count):
            if index != node_index:
                sorted_distances.append(str(self.distances[index]))

        return sorted_distances


def main():
    ''' Main function '''

    num_queries = int(input())
    for _ in range(num_queries):
        node_count, edge_count = [int(value) for value in input().split()]
        graph = Graph(node_count)

        for _ in range(edge_count):
            node_1, node_2 = [int(x) for x in input().split()]
            graph.connect(node_1 - 1, node_2 - 1)

        starting_node_index = int(input())
        distances = graph.find_all_distances(starting_node_index - 1)
        print(" ".join(distances))

if __name__ == '__main__':
    main()
