import tkinter as tk
from tkinter import ttk

from Astar import AStarSearch, CostPath
from bfs import bfs
from dfs import dfs
from dls import dls
from iterative import iterative


class TreeNode:
    def __init__(self, value, cost):
        self.value = value
        self.cost = cost
        self.left = None
        self.right = None

def create_tree():
    # Create tree nodes with different costs
    root = TreeNode(1, 0)
    left_child = TreeNode(4, 2)
    right_child = TreeNode(5, 1)
    right_child_left = TreeNode(7, 3)
    right_child_right = TreeNode(8, 4)
    left_child_left = TreeNode(9, 5)
    left_child_right = TreeNode(3, 1)

    # Build tree structure
    root.left = left_child
    root.right = right_child
    right_child.left = right_child_left
    right_child.right = right_child_right
    left_child.left = left_child_left
    left_child.right = left_child_right

    return root  # Return the root of the tree

def draw_tree(canvas, root, x, y, x_offset):
    node_radius = 20

    # Draw the current node
    canvas.create_oval(x - node_radius, y - node_radius, x + node_radius, y + node_radius, fill='lightblue')
    canvas.create_text(x, y, text=root.value)

    # Calculate the x-coordinate for the children nodes
    child_x = x - x_offset

    if root.left:
        child_y = y + 80
        canvas.create_line(x, y + node_radius, child_x, child_y - node_radius)
        # Draw the cost label for the left edge
        canvas.create_text((x + child_x) / 2, (y + child_y) / 2, text=str(root.left.cost))

        draw_tree(canvas, root.left, child_x, child_y, x_offset / 2)

    if root.right:
        child_y = y + 80
        canvas.create_line(x, y + node_radius, x + x_offset, child_y - node_radius)
        # Draw the cost label for the right edge
        canvas.create_text((x + x + x_offset) / 2, (y + child_y) / 2, text=str(root.right.cost))

        draw_tree(canvas, root.right, x + x_offset, child_y, x_offset / 2)

def search_algorithm_selected():
    graph = {1: [4, 5], 4: [9, 3], 5: [7, 8], 7: [], 8: [], 9: [], 3: []}  # direction graph
    selected_algorithm = algorithm_combobox.get()
    if selected_algorithm == "DFS":
        path, visited = dfs(graph, 7)
        print("found goal  path :", path, "and visited node :", visited, sep=" ", end="")
    elif selected_algorithm == "BFS":
        path, visited = bfs(graph, 7)
        if path:
            print("found goal  path :", path, "and visited node :", visited, sep=" ", end="")
        else:
            print("goal not found")
    elif selected_algorithm == "DLS":
        visited, path = [], []
        limit = 2
        path = dls(list(graph.keys())[0], 7, graph, visited, path, limit)
        if path:
            print(path)
        else:
            print("goal not found")
    elif selected_algorithm == "Iterative Deepening":

        goal, maxD = 7, 4

        for i in range(1, maxD):
            path, visited = iterative(graph, goal, i)
            if path:
                print("found goal in level :", i, "and path :", path, "and visited node :", visited, sep=" ",
                      end="")
                break
        else:
            print("goal not found")
    elif selected_algorithm == "A*":
        path = AStarSearch( 1, 7)
        if path:
            print("found Solution :", path)
            print("and the cost is :", CostPath(path))
        else:
            print("error message")


root = tk.Tk()
root.title("Search Tree GUI")

# Create a Canvas to draw the search tree
canvas = tk.Canvas(root, width=600, height=400)
canvas.pack()

# Create the search tree
tree = create_tree()

# Draw the search tree
draw_tree(canvas, tree, 300, 50, 100)

# Create a combobox for selecting the search algorithm
algorithm_combobox = ttk.Combobox(root, values=["DFS", "BFS", "DLS", "Iterative Deepening", "A*"])
algorithm_combobox.set("DFS")
# Set the default algorithm
algorithm_combobox.pack()

# Button to trigger the search algorithm selection
algorithm_button = tk.Button(root, text="Select Algorithm", command=search_algorithm_selected)
algorithm_button.pack()

root.mainloop()