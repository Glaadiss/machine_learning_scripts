import numpy as np
from functools import reduce


class Tree:
    def __init__(self, data, left=None, right=None):
        self.left = left
        self.right = right
        self.data = data


d = Tree([32, 24], left=Tree([23, 8]), right=Tree([9, 16]))


def get_gini(selections):
    total = np.sum(selections)
    return 1 - reduce(
        lambda acc, curr: acc + (curr / total) ** 2,
        selections,
        0)


def get_class_error(selections):
    return 1 - (np.max(selections) / np.sum(selections))


def get_entropy(selections):
    total = np.sum(selections)
    return 1 - reduce(
        lambda acc, curr: acc + (curr / total) * np.log2(curr / total),
        selections,
        0)


def get_purity_gain(data, method_string='gini'):
    """
    Calculate purity gain for tree

    :param method_string: 'gini' | 'class_error' | 'entropy'
    :param data: e.g Tree(
                        [32, 24],
                        left=Tree([23, 8]),
                        right=Tree([9, 16]))
    :return: purity gain e.g. 0.4
    """
    method = {
        "gini": get_gini,
        "class_error": get_class_error,
        "entropy": get_class_error
    }[method_string]

    def calculate_purity(tree):
        total = sum(tree.data)
        if tree.left is None:
            return method(tree.data) * total

        return method(tree.data) - calculate_purity(tree.left) / total - calculate_purity(tree.right) / total

    return calculate_purity(data)


print(get_purity_gain(d, 'class_error'))
