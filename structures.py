from math import sqrt
from symbol import continue_stmt


class Node:
    def __init__(self, position, parent):
        """
        Simple node with the purpuse of being used in teh A* algorithm

        :param position: is atuple of int elemnts of form: (x,y)
        where y is the depth 0 <= y < m | m is the size of a column of the maze
        and x is the length 0 <= x < n | n is the size of a line of the maze

        :param parent: is an object of type Node
        """

        self.position = position
        self.parent = parent

        self.f = 0
        self.g = 0
        self.h = 0

    def compute_f(self, end_node):
        self.g = self.parent.g + 1
        self.h = sqrt(
            (self.position[0] - end_node.position[0]) ** 2
            + (self.position[1] - end_node.position[1]) ** 2
        )
        self.f = self.g + self.h

    def get_neighbours(self):
        """
        Returns a list of neighbours of a node that are found up,right,down and left
        """
        neighbours = []

        # move the point W,E,N,S
        for move_position in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbours.append(
                Node(
                    position=(
                        self.position[0] + move_position[0],
                        self.position[1] + move_position[1],
                    ),
                    parent=self,
                )
            )

        return neighbours

    def __eq__(self, other):
        return self.position == other.position

    def __repr__(self):
        return str(self.position)
