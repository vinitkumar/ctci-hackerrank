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

        node_set = self.edges[node_2]
        node_set.add(node_1)
        self.edges[node_2] = node_set

        # print("connecting", node_1, "and", node_2)
        # print(node_set)
        # print(self.edges)

    def find_all_distances(self, node_index):
        '''
        calculates distance between the given node and all other nodes
        in the graph
        '''
        # print(self.edges)
        possible_paths = queue.Queue()
        # start_node = (node_index, 0)  # (index, relative_distance)
        possible_paths.put(node_index)
        traversed_nodes = set([node_index])
        self.distances[node_index] = 0
        # print("starting with", node_index)

        while not possible_paths.empty():
            current_node = possible_paths.get()
            # print("working on node ", current_node)
            # print("children are ", self.edges[current_node])

            distance = int(self.distances[current_node] + DISTANCE_FACTOR)
            # print("calculated distance: ", distance)
            for child_node in self.edges[current_node]:
                # print("child_node:", child_node, ", distance:", distance)
                if child_node not in traversed_nodes:
                    self.distances[child_node] = distance
                    possible_paths.put(child_node)
                    traversed_nodes.add(child_node)
            # print("distances ", self.distances)

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


def main_test():
    ''' Testing Main function '''

    input_file_path = "solutions/tmp/input06.txt"
    input_file = open(input_file_path)

    num_queries = int(input_file.readline().strip())
    for _ in range(num_queries):
        node_count, edge_count = \
            [int(value) for value in input_file.readline().strip().split()]
        graph = Graph(node_count)

        for _ in range(edge_count):
            node_1, node_2 = \
                [int(x) for x in input_file.readline().strip().split()]
            graph.connect(node_1 - 1, node_2 - 1)

        starting_node_index = int(input_file.readline().strip())
        distances = graph.find_all_distances(starting_node_index - 1)
        print(" ".join(distances))

    input_file.close()

if __name__ == '__main__':
    main()
    # main_test()
