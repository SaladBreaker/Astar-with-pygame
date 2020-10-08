from structures import Node


def sorted_insert(opened_list, node):
    """
    Performs a sorted insert in the list

    :param opened_list: that is sorted ascending (0 to len)

    :param node: and objet of type Node that is going to be inserted such that the list remains sorted
    """
    for index in range(len(opened_list)):
        if opened_list[index].f > node.f:
            return opened_list[:index] + [node] + opened_list[index:]

    return opened_list + [node]


def get_path_astart(maze, start, end):
    """
    returns  a list with the best path from the start to the end

    :param maze: matrice where 0 represents a walkable cell and 1 is a obstacle cell

    :param start: typle of form (x,y)

    :param end: typle of form (x,y)
    """
    opened_list = []
    closed_list = []

    column_length = len(maze)
    line_length = len(maze[0])

    start_node = Node(start, None)
    end_node = Node(end, None)

    opened_list.append(start_node)

    while opened_list:
        current_node = opened_list.pop(0)
        closed_list.append(current_node)
        print(f"On node: {current_node.position}")
        # print(f"On : {opened_list}")
        # print(f"Off: {closed_list}")

        if current_node == end_node:
            print("Found it!")
            return

        neighbours = current_node.get_neighbours()
        for neighbour in neighbours:

            # check is the neighbour  is outside the maze
            if (
                neighbour.position[0] >= line_length
                or neighbour.position[0] < 0
                or neighbour.position[1] >= column_length
                or neighbour.position[1] < 0
            ):
                continue

            # check is the neighbour is an obstacle
            if maze[neighbour.position[0]][neighbour.position[1]] == 1:
                continue

            if neighbour in closed_list:
                continue

            neighbour.compute_f(end_node)

            # if the neighbour is in the opened list check if the new one is a better fit
            if neighbour in opened_list:
                index = opened_list.index(neighbour)

                if opened_list[index].f > neighbour.f:
                    opened_list[index] = neighbour

                continue

            opened_list = sorted_insert(opened_list, neighbour)


if __name__ == "__main__":
    maze = [[0, 0, 0, 0], [0, 1, 0, 1], [0, 0, 0, 1], [0, 0, 1, 0]]

    start = (0, 0)
    end = (3, 3)
    get_path_astart(maze, start, end)
