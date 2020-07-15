from ppbtree import *


class Node:
    def __init__(self, pivot_value, start, end, values, left_node=None, right_node=None):
        self.pivot_value = pivot_value
        self.left_node = left_node
        self.right_node = right_node
        self.start = start
        self.end = end
        self.values = values

    def __str__(self):
        if self.pivot_value is not None:
            return str(self.pivot_value)
        else:
            return str(self.values[self.start: self.end])


def common(l1, l2):
    pivot_list, traverse_list = __get_pivot_traverse(l1, l2)
    return __process(pivot_list, traverse_list)


def __get_pivot_traverse(l1, l2):
    k1 = len(l1)
    k2 = len(l2)
    pivot_list = l1
    traverse_list = l2
    if k1 > k2:
        pivot_list, traverse_list = l2, l1
    return pivot_list, traverse_list


def __process(pivot_list, traverse_list):
    root = Node(None, 0, len(traverse_list), traverse_list)
    common_elements = []
    for pivot in pivot_list:
        if __traverse(root, pivot):
            common_elements.append(pivot)
    # print_tree(root, left_child='left_node', right_child='right_node')
    return common_elements


def __traverse(node, pivot):
    if node.pivot_value is None:
        is_common, q = __partition(pivot, node)
        left_node = Node(None, node.start, q, node.values)
        right_node = Node(None, q, node.end, node.values)
        node.left_node = left_node
        node.right_node = right_node
        node.pivot_value = pivot
        return is_common
    elif node.pivot_value == pivot:
        return False
    elif node.pivot_value < pivot:
        return __traverse(node.right_node, pivot)
    else:
        return __traverse(node.left_node, pivot)


def __partition(pivot, node):
    is_common = False
    q = node.start
    for p in range(node.start, node.end):
        value = node.values[p]
        if value <= pivot:
            if value == pivot:
                is_common = True
            node.values[p], node.values[q] = node.values[q], node.values[p]
            q += 1
    return is_common, q
