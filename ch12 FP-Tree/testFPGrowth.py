# ====================================================================================
# Author: Junbo Xin
# Date: 2015/02/17
# Description:  Frequent Pattern Growth
# ====================================================================================

from numpy import *
import fpGrowth


def test_tree_node():
    root = fpGrowth.TreeNode('pyramid', 9, None)
    root.children['eye'] = fpGrowth.TreeNode('eye', 13, None)
    root.display()
    root.children['phoenix'] = fpGrowth.TreeNode('phoenix', 3, None)
    root.display()


def test_simple():
    data_set = fpGrowth.load_simple_data()
    dic = fpGrowth.create_init_set(data_set)
    print dic


def test_create_tree():
    data_set = fpGrowth.load_simple_data()
    init_set = fpGrowth.create_init_set(data_set)
    tree, head_table = fpGrowth.create_tree(init_set, 3)


def main():
    # test_simple()
    # test_tree_node()
    test_create_tree()


if __name__ == '__main__':
    main()