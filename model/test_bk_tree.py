from bk_tree import BKNode, BKTree


class TestBK:

    def test1(self):
        test_tree = BKTree()
        test_tree.set_up_from_file("model/demo_wordlist.txt")
        assert len(test_tree.tree_root.get_children_with_distance()) == 4

    def testweight(self):
        test_tree = BKTree()
        test_tree.set_up_from_file("model/demo_wordlist.txt")
        assert test_tree.tree_root.get_child_distances()[0] == 1