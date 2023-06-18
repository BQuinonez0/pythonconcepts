# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 16:47:24 2023

@author: Britney
"""

import matplotlib.pyplot as plt

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)

def plot_tree(node, ax, x_pos, y_pos, x_step, y_step):
    ax.text(x_pos, y_pos, str(node.value), ha='center', va='center', bbox=dict(facecolor='white', edgecolor='black', boxstyle='circle'))

    num_children = len(node.children)
    if num_children == 0:
        return

    x_start = x_pos - x_step * (num_children - 1) / 2
    for child in node.children:
        ax.plot([x_pos, x_start], [y_pos, y_pos-y_step], color='black')
        plot_tree(child, ax, x_start, y_pos-y_step, x_step, y_step)
        x_start += x_step

# Create the nodes
root = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)

# Build the tree structure
root.add_child(node2)
root.add_child(node3)
node2.add_child(node4)
node2.add_child(node5)
node3.add_child(node6)

# Create the plot
fig, ax = plt.subplots(figsize=(8, 6))
ax.axis('off')

# Set the parameters for tree visualization
x_step = 1
y_step = 1

# Plot the tree
plot_tree(root, ax, 0, 0, x_step, y_step)

# Show the plot
plt.show()
