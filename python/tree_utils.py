"""
Various generally tree tools.
"""

def display(node, level=0):
    """
    Recursively display a tree rooted at node. It's not perfect but it'll
    help visualize a tree.
    """
    if level == 0:
	prefix = ""
    else:
	prefix = "    "*(max(0, level - 1)) + "|----"
    print(prefix + str(node.value))
    if node.left is not None:
	display(node.left, level + 1)
    if node.right is not None:
	display(node.right, level + 1)
